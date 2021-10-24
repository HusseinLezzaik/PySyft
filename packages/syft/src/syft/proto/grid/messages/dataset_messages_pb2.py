# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/grid/messages/dataset_messages.proto
"""Generated protocol buffer code."""
# third party
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# syft absolute
from syft.proto.core.common import (
    common_object_pb2 as proto_dot_core_dot_common_dot_common__object__pb2,
)
from syft.proto.core.io import address_pb2 as proto_dot_core_dot_io_dot_address__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/grid/messages/dataset_messages.proto',
  package='syft.grid.messages',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*proto/grid/messages/dataset_messages.proto\x12\x12syft.grid.messages\x1a%proto/core/common/common_object.proto\x1a\x1bproto/core/io/address.proto\"\xac\x02\n\x14\x43reateDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x0f\n\x07\x64\x61taset\x18\x03 \x01(\x0c\x12H\n\x08metadata\x18\x04 \x03(\x0b\x32\x36.syft.grid.messages.CreateDatasetMessage.MetadataEntry\x12\'\n\x08reply_to\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x10\n\x08platform\x18\x06 \x01(\t\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x9f\x01\n\x11GetDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\ndataset_id\x18\x03 \x01(\x03\x12\'\n\x08reply_to\x18\x04 \x01(\x0b\x32\x15.syft.core.io.Address\"\xdc\x01\n\x12GetDatasetResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12\x46\n\x08metadata\x18\x02 \x03(\x0b\x32\x34.syft.grid.messages.GetDatasetResponse.MetadataEntry\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x12GetDatasetsMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\'\n\x08reply_to\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\"\xd7\x02\n\x13GetDatasetsResponse\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12M\n\tmetadatas\x18\x02 \x03(\x0b\x32:.syft.grid.messages.GetDatasetsResponse.metadata_container\x12&\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x15.syft.core.io.Address\x1a\xa1\x01\n\x12metadata_container\x12Z\n\x08metadata\x18\x01 \x03(\x0b\x32H.syft.grid.messages.GetDatasetsResponse.metadata_container.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\"\x9d\x02\n\x14UpdateDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\ndataset_id\x18\x03 \x01(\x03\x12H\n\x08metadata\x18\x04 \x03(\x0b\x32\x36.syft.grid.messages.UpdateDatasetMessage.MetadataEntry\x12\'\n\x08reply_to\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Address\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb9\x01\n\x14\x44\x65leteDatasetMessage\x12%\n\x06msg_id\x18\x01 \x01(\x0b\x32\x15.syft.core.common.UID\x12&\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32\x15.syft.core.io.Address\x12\x12\n\ndataset_id\x18\x03 \x01(\t\x12\x15\n\rbin_object_id\x18\x04 \x01(\t\x12\'\n\x08reply_to\x18\x05 \x01(\x0b\x32\x15.syft.core.io.Addressb\x06proto3'
  ,
  dependencies=[proto_dot_core_dot_common_dot_common__object__pb2.DESCRIPTOR,proto_dot_core_dot_io_dot_address__pb2.DESCRIPTOR,])




_CREATEDATASETMESSAGE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='syft.grid.messages.CreateDatasetMessage.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft.grid.messages.CreateDatasetMessage.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft.grid.messages.CreateDatasetMessage.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=435,
)

_CREATEDATASETMESSAGE = _descriptor.Descriptor(
  name='CreateDatasetMessage',
  full_name='syft.grid.messages.CreateDatasetMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.CreateDatasetMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.CreateDatasetMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='syft.grid.messages.CreateDatasetMessage.dataset', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='syft.grid.messages.CreateDatasetMessage.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.grid.messages.CreateDatasetMessage.reply_to', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='platform', full_name='syft.grid.messages.CreateDatasetMessage.platform', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CREATEDATASETMESSAGE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=435,
)


_GETDATASETMESSAGE = _descriptor.Descriptor(
  name='GetDatasetMessage',
  full_name='syft.grid.messages.GetDatasetMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.GetDatasetMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.GetDatasetMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='syft.grid.messages.GetDatasetMessage.dataset_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.grid.messages.GetDatasetMessage.reply_to', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=597,
)


_GETDATASETRESPONSE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='syft.grid.messages.GetDatasetResponse.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft.grid.messages.GetDatasetResponse.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft.grid.messages.GetDatasetResponse.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=435,
)

_GETDATASETRESPONSE = _descriptor.Descriptor(
  name='GetDatasetResponse',
  full_name='syft.grid.messages.GetDatasetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.GetDatasetResponse.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='syft.grid.messages.GetDatasetResponse.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.GetDatasetResponse.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETDATASETRESPONSE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=600,
  serialized_end=820,
)


_GETDATASETSMESSAGE = _descriptor.Descriptor(
  name='GetDatasetsMessage',
  full_name='syft.grid.messages.GetDatasetsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.GetDatasetsMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.GetDatasetsMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.grid.messages.GetDatasetsMessage.reply_to', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=823,
  serialized_end=963,
)


_GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='syft.grid.messages.GetDatasetsResponse.metadata_container.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft.grid.messages.GetDatasetsResponse.metadata_container.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft.grid.messages.GetDatasetsResponse.metadata_container.MetadataEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1262,
  serialized_end=1309,
)

_GETDATASETSRESPONSE_METADATA_CONTAINER = _descriptor.Descriptor(
  name='metadata_container',
  full_name='syft.grid.messages.GetDatasetsResponse.metadata_container',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='syft.grid.messages.GetDatasetsResponse.metadata_container.metadata', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1148,
  serialized_end=1309,
)

_GETDATASETSRESPONSE = _descriptor.Descriptor(
  name='GetDatasetsResponse',
  full_name='syft.grid.messages.GetDatasetsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.GetDatasetsResponse.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadatas', full_name='syft.grid.messages.GetDatasetsResponse.metadatas', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.GetDatasetsResponse.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETDATASETSRESPONSE_METADATA_CONTAINER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=966,
  serialized_end=1309,
)


_UPDATEDATASETMESSAGE_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='syft.grid.messages.UpdateDatasetMessage.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='syft.grid.messages.UpdateDatasetMessage.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='syft.grid.messages.UpdateDatasetMessage.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=388,
  serialized_end=435,
)

_UPDATEDATASETMESSAGE = _descriptor.Descriptor(
  name='UpdateDatasetMessage',
  full_name='syft.grid.messages.UpdateDatasetMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.UpdateDatasetMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.UpdateDatasetMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='syft.grid.messages.UpdateDatasetMessage.dataset_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='syft.grid.messages.UpdateDatasetMessage.metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.grid.messages.UpdateDatasetMessage.reply_to', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_UPDATEDATASETMESSAGE_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1312,
  serialized_end=1597,
)


_DELETEDATASETMESSAGE = _descriptor.Descriptor(
  name='DeleteDatasetMessage',
  full_name='syft.grid.messages.DeleteDatasetMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg_id', full_name='syft.grid.messages.DeleteDatasetMessage.msg_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='syft.grid.messages.DeleteDatasetMessage.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='syft.grid.messages.DeleteDatasetMessage.dataset_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bin_object_id', full_name='syft.grid.messages.DeleteDatasetMessage.bin_object_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reply_to', full_name='syft.grid.messages.DeleteDatasetMessage.reply_to', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1600,
  serialized_end=1785,
)

_CREATEDATASETMESSAGE_METADATAENTRY.containing_type = _CREATEDATASETMESSAGE
_CREATEDATASETMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_CREATEDATASETMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_CREATEDATASETMESSAGE.fields_by_name['metadata'].message_type = _CREATEDATASETMESSAGE_METADATAENTRY
_CREATEDATASETMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETRESPONSE_METADATAENTRY.containing_type = _GETDATASETRESPONSE
_GETDATASETRESPONSE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETRESPONSE.fields_by_name['metadata'].message_type = _GETDATASETRESPONSE_METADATAENTRY
_GETDATASETRESPONSE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETSMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETSMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETSMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY.containing_type = _GETDATASETSRESPONSE_METADATA_CONTAINER
_GETDATASETSRESPONSE_METADATA_CONTAINER.fields_by_name['metadata'].message_type = _GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY
_GETDATASETSRESPONSE_METADATA_CONTAINER.containing_type = _GETDATASETSRESPONSE
_GETDATASETSRESPONSE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_GETDATASETSRESPONSE.fields_by_name['metadatas'].message_type = _GETDATASETSRESPONSE_METADATA_CONTAINER
_GETDATASETSRESPONSE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEDATASETMESSAGE_METADATAENTRY.containing_type = _UPDATEDATASETMESSAGE
_UPDATEDATASETMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_UPDATEDATASETMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_UPDATEDATASETMESSAGE.fields_by_name['metadata'].message_type = _UPDATEDATASETMESSAGE_METADATAENTRY
_UPDATEDATASETMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_DELETEDATASETMESSAGE.fields_by_name['msg_id'].message_type = proto_dot_core_dot_common_dot_common__object__pb2._UID
_DELETEDATASETMESSAGE.fields_by_name['address'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
_DELETEDATASETMESSAGE.fields_by_name['reply_to'].message_type = proto_dot_core_dot_io_dot_address__pb2._ADDRESS
DESCRIPTOR.message_types_by_name['CreateDatasetMessage'] = _CREATEDATASETMESSAGE
DESCRIPTOR.message_types_by_name['GetDatasetMessage'] = _GETDATASETMESSAGE
DESCRIPTOR.message_types_by_name['GetDatasetResponse'] = _GETDATASETRESPONSE
DESCRIPTOR.message_types_by_name['GetDatasetsMessage'] = _GETDATASETSMESSAGE
DESCRIPTOR.message_types_by_name['GetDatasetsResponse'] = _GETDATASETSRESPONSE
DESCRIPTOR.message_types_by_name['UpdateDatasetMessage'] = _UPDATEDATASETMESSAGE
DESCRIPTOR.message_types_by_name['DeleteDatasetMessage'] = _DELETEDATASETMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateDatasetMessage = _reflection.GeneratedProtocolMessageType('CreateDatasetMessage', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _CREATEDATASETMESSAGE_METADATAENTRY,
    '__module__' : 'proto.grid.messages.dataset_messages_pb2'
    # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateDatasetMessage.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _CREATEDATASETMESSAGE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.CreateDatasetMessage)
  })
_sym_db.RegisterMessage(CreateDatasetMessage)
_sym_db.RegisterMessage(CreateDatasetMessage.MetadataEntry)

GetDatasetMessage = _reflection.GeneratedProtocolMessageType('GetDatasetMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETMESSAGE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetMessage)
  })
_sym_db.RegisterMessage(GetDatasetMessage)

GetDatasetResponse = _reflection.GeneratedProtocolMessageType('GetDatasetResponse', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _GETDATASETRESPONSE_METADATAENTRY,
    '__module__' : 'proto.grid.messages.dataset_messages_pb2'
    # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetResponse.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _GETDATASETRESPONSE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetResponse)
  })
_sym_db.RegisterMessage(GetDatasetResponse)
_sym_db.RegisterMessage(GetDatasetResponse.MetadataEntry)

GetDatasetsMessage = _reflection.GeneratedProtocolMessageType('GetDatasetsMessage', (_message.Message,), {
  'DESCRIPTOR' : _GETDATASETSMESSAGE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetsMessage)
  })
_sym_db.RegisterMessage(GetDatasetsMessage)

GetDatasetsResponse = _reflection.GeneratedProtocolMessageType('GetDatasetsResponse', (_message.Message,), {

  'metadata_container' : _reflection.GeneratedProtocolMessageType('metadata_container', (_message.Message,), {

    'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
      'DESCRIPTOR' : _GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY,
      '__module__' : 'proto.grid.messages.dataset_messages_pb2'
      # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetsResponse.metadata_container.MetadataEntry)
      })
    ,
    'DESCRIPTOR' : _GETDATASETSRESPONSE_METADATA_CONTAINER,
    '__module__' : 'proto.grid.messages.dataset_messages_pb2'
    # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetsResponse.metadata_container)
    })
  ,
  'DESCRIPTOR' : _GETDATASETSRESPONSE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.GetDatasetsResponse)
  })
_sym_db.RegisterMessage(GetDatasetsResponse)
_sym_db.RegisterMessage(GetDatasetsResponse.metadata_container)
_sym_db.RegisterMessage(GetDatasetsResponse.metadata_container.MetadataEntry)

UpdateDatasetMessage = _reflection.GeneratedProtocolMessageType('UpdateDatasetMessage', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _UPDATEDATASETMESSAGE_METADATAENTRY,
    '__module__' : 'proto.grid.messages.dataset_messages_pb2'
    # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateDatasetMessage.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _UPDATEDATASETMESSAGE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.UpdateDatasetMessage)
  })
_sym_db.RegisterMessage(UpdateDatasetMessage)
_sym_db.RegisterMessage(UpdateDatasetMessage.MetadataEntry)

DeleteDatasetMessage = _reflection.GeneratedProtocolMessageType('DeleteDatasetMessage', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDATASETMESSAGE,
  '__module__' : 'proto.grid.messages.dataset_messages_pb2'
  # @@protoc_insertion_point(class_scope:syft.grid.messages.DeleteDatasetMessage)
  })
_sym_db.RegisterMessage(DeleteDatasetMessage)


_CREATEDATASETMESSAGE_METADATAENTRY._options = None
_GETDATASETRESPONSE_METADATAENTRY._options = None
_GETDATASETSRESPONSE_METADATA_CONTAINER_METADATAENTRY._options = None
_UPDATEDATASETMESSAGE_METADATAENTRY._options = None
# @@protoc_insertion_point(module_scope)
