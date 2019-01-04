# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/storage/BigTable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feast.types import Value_pb2 as feast_dot_types_dot_Value__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/storage/BigTable.proto',
  package='feast.storage',
  syntax='proto3',
  serialized_options=_b('\n\rfeast.storageB\rBigTableProtoZ8github.com/gojek/feast/protos/generated/go/feast/storage'),
  serialized_pb=_b('\n\x1c\x66\x65\x61st/storage/BigTable.proto\x12\rfeast.storage\x1a\x17\x66\x65\x61st/types/Value.proto\"O\n\x0e\x42igTableRowKey\x12\x12\n\nsha1Prefix\x18\x01 \x01(\t\x12\x11\n\tentityKey\x18\x02 \x01(\t\x12\x16\n\x0ereversedMillis\x18\x03 \x01(\tBX\n\rfeast.storageB\rBigTableProtoZ8github.com/gojek/feast/protos/generated/go/feast/storageb\x06proto3')
  ,
  dependencies=[feast_dot_types_dot_Value__pb2.DESCRIPTOR,])




_BIGTABLEROWKEY = _descriptor.Descriptor(
  name='BigTableRowKey',
  full_name='feast.storage.BigTableRowKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sha1Prefix', full_name='feast.storage.BigTableRowKey.sha1Prefix', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entityKey', full_name='feast.storage.BigTableRowKey.entityKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reversedMillis', full_name='feast.storage.BigTableRowKey.reversedMillis', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=72,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['BigTableRowKey'] = _BIGTABLEROWKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BigTableRowKey = _reflection.GeneratedProtocolMessageType('BigTableRowKey', (_message.Message,), dict(
  DESCRIPTOR = _BIGTABLEROWKEY,
  __module__ = 'feast.storage.BigTable_pb2'
  # @@protoc_insertion_point(class_scope:feast.storage.BigTableRowKey)
  ))
_sym_db.RegisterMessage(BigTableRowKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
