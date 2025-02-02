# future
from __future__ import annotations

# stdlib
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

# third party
from nacl.signing import VerifyKey
from typing_extensions import final

# relative
from .....common.serde.serializable import serializable
from ....abstract.node_service_interface import NodeServiceInterface
from ...node_table.node import NoSQLNode
from ...node_table.node import NoSQLNodeRoute
from ..generic_payload.messages import GenericPayloadMessage
from ..generic_payload.messages import GenericPayloadMessageWithReply
from ..generic_payload.messages import GenericPayloadReplyMessage


@serializable(recursive_serde=True)
@final
class PeerDiscoveryMessage(GenericPayloadMessage):
    ...


@serializable(recursive_serde=True)
@final
class PeerDiscoveryReplyMessage(GenericPayloadReplyMessage):
    ...


def node_id_to_peer_route_metadata(node_document: NoSQLNode) -> List[Dict[str, Any]]:
    routes: List[NoSQLNodeRoute] = node_document.node_route
    routes_meta = []
    for route in routes:
        peer_route: Dict[str, Any] = {}
        peer_route["id"] = node_document.node_uid
        peer_route["name"] = node_document.node_name
        peer_route["host_or_ip"] = route.host_or_ip
        peer_route["is_vpn"] = route.is_vpn
        peer_route["private"] = route.private
        peer_route["protocol"] = route.protocol
        peer_route["port"] = route.port
        routes_meta.append(peer_route)
    return routes_meta


@serializable(recursive_serde=True)
@final
class PeerDiscoveryMessageWithReply(GenericPayloadMessageWithReply):
    message_type = PeerDiscoveryMessage
    message_reply_type = PeerDiscoveryReplyMessage

    def run(
        self, node: NodeServiceInterface, verify_key: Optional[VerifyKey] = None
    ) -> Dict[str, Any]:
        try:
            peer_routes = []
            for peer in node.node.all():
                peer_routes += node_id_to_peer_route_metadata(node_document=peer)
            return {"status": "ok", "data": peer_routes}
        except Exception as e:
            print(f"Failed to run {type(self)}", self.kwargs, e)
            return {"status": "error"}


@serializable(recursive_serde=True)
@final
class GetPeerInfoMessageWithReply(GenericPayloadMessageWithReply):
    message_type = PeerDiscoveryMessage
    message_reply_type = PeerDiscoveryReplyMessage

    def run(
        self, node: NodeServiceInterface, verify_key: Optional[VerifyKey] = None
    ) -> Dict[str, Any]:
        try:
            # TODO: handle multiple routes and possibly prefer vpn connections
            peer = node.node.first(node_uid=str(self.kwargs["uid"]))
            peer_route: Dict[str, Any] = {}
            if peer:
                for route in peer.node_route:
                    peer_route["id"] = peer.node_uid
                    peer_route["name"] = peer.node_name
                    peer_route["host_or_ip"] = route.host_or_ip
                    peer_route["is_vpn"] = route.is_vpn
            return {"status": "ok", "data": peer_route}
        except Exception as e:
            print(f"Failed to run {type(self)}", self.kwargs, e)
            return {"status": "error"}
