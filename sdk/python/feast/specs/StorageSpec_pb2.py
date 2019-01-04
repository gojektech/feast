# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/specs/StorageSpec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/specs/StorageSpec.proto',
  package='feast.specs',
  syntax='proto3',
  serialized_options=_b('\n\013feast.specsB\020StorageSpecProtoZ6github.com/gojek/feast/protos/generated/go/feast/specs'),
  serialized_pb=_b('\n\x1d\x66\x65\x61st/specs/StorageSpec.proto\x12\x0b\x66\x65\x61st.specs\"\x8f\x01\n\x0bStorageSpec\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x36\n\x07options\x18\x03 \x03(\x0b\x32%.feast.specs.StorageSpec.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42W\n\x0b\x66\x65\x61st.specsB\x10StorageSpecProtoZ6github.com/gojek/feast/protos/generated/go/feast/specsb\x06proto3')
)




_STORAGESPEC_OPTIONSENTRY = _descriptor.Descriptor(
  name='OptionsEntry',
  full_name='feast.specs.StorageSpec.OptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.specs.StorageSpec.OptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.specs.StorageSpec.OptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=190,
)

_STORAGESPEC = _descriptor.Descriptor(
  name='StorageSpec',
  full_name='feast.specs.StorageSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='feast.specs.StorageSpec.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.specs.StorageSpec.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='feast.specs.StorageSpec.options', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STORAGESPEC_OPTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=190,
)

_STORAGESPEC_OPTIONSENTRY.containing_type = _STORAGESPEC
_STORAGESPEC.fields_by_name['options'].message_type = _STORAGESPEC_OPTIONSENTRY
DESCRIPTOR.message_types_by_name['StorageSpec'] = _STORAGESPEC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StorageSpec = _reflection.GeneratedProtocolMessageType('StorageSpec', (_message.Message,), dict(

  OptionsEntry = _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), dict(
    DESCRIPTOR = _STORAGESPEC_OPTIONSENTRY,
    __module__ = 'feast.specs.StorageSpec_pb2'
    # @@protoc_insertion_point(class_scope:feast.specs.StorageSpec.OptionsEntry)
    ))
  ,
  DESCRIPTOR = _STORAGESPEC,
  __module__ = 'feast.specs.StorageSpec_pb2'
  # @@protoc_insertion_point(class_scope:feast.specs.StorageSpec)
  ))
_sym_db.RegisterMessage(StorageSpec)
_sym_db.RegisterMessage(StorageSpec.OptionsEntry)


DESCRIPTOR._options = None
_STORAGESPEC_OPTIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
