# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/types/FeatureRowExtended.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from feast.types import FeatureRow_pb2 as feast_dot_types_dot_FeatureRow__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/types/FeatureRowExtended.proto',
  package='feast.types',
  syntax='proto3',
  serialized_options=_b('\n\013feast.typesB\027FeatureRowExtendedProtoZ6github.com/gojek/feast/protos/generated/go/feast/types'),
  serialized_pb=_b('\n$feast/types/FeatureRowExtended.proto\x12\x0b\x66\x65\x61st.types\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1c\x66\x65\x61st/types/FeatureRow.proto\"N\n\x05\x45rror\x12\r\n\x05\x63\x61use\x18\x01 \x01(\t\x12\x11\n\ttransform\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x12\n\nstackTrace\x18\x04 \x01(\t\">\n\x07\x41ttempt\x12\x10\n\x08\x61ttempts\x18\x01 \x01(\x05\x12!\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.feast.types.Error\"\x94\x01\n\x12\x46\x65\x61tureRowExtended\x12$\n\x03row\x18\x01 \x01(\x0b\x32\x17.feast.types.FeatureRow\x12)\n\x0blastAttempt\x18\x02 \x01(\x0b\x32\x14.feast.types.Attempt\x12-\n\tfirstSeen\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB^\n\x0b\x66\x65\x61st.typesB\x17\x46\x65\x61tureRowExtendedProtoZ6github.com/gojek/feast/protos/generated/go/feast/typesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,feast_dot_types_dot_FeatureRow__pb2.DESCRIPTOR,])




_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='feast.types.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cause', full_name='feast.types.Error.cause', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transform', full_name='feast.types.Error.transform', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='feast.types.Error.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stackTrace', full_name='feast.types.Error.stackTrace', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=116,
  serialized_end=194,
)


_ATTEMPT = _descriptor.Descriptor(
  name='Attempt',
  full_name='feast.types.Attempt',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attempts', full_name='feast.types.Attempt.attempts', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='feast.types.Attempt.error', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=196,
  serialized_end=258,
)


_FEATUREROWEXTENDED = _descriptor.Descriptor(
  name='FeatureRowExtended',
  full_name='feast.types.FeatureRowExtended',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='feast.types.FeatureRowExtended.row', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastAttempt', full_name='feast.types.FeatureRowExtended.lastAttempt', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='firstSeen', full_name='feast.types.FeatureRowExtended.firstSeen', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=261,
  serialized_end=409,
)

_ATTEMPT.fields_by_name['error'].message_type = _ERROR
_FEATUREROWEXTENDED.fields_by_name['row'].message_type = feast_dot_types_dot_FeatureRow__pb2._FEATUREROW
_FEATUREROWEXTENDED.fields_by_name['lastAttempt'].message_type = _ATTEMPT
_FEATUREROWEXTENDED.fields_by_name['firstSeen'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['Attempt'] = _ATTEMPT
DESCRIPTOR.message_types_by_name['FeatureRowExtended'] = _FEATUREROWEXTENDED
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'feast.types.FeatureRowExtended_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Error)
  ))
_sym_db.RegisterMessage(Error)

Attempt = _reflection.GeneratedProtocolMessageType('Attempt', (_message.Message,), dict(
  DESCRIPTOR = _ATTEMPT,
  __module__ = 'feast.types.FeatureRowExtended_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.Attempt)
  ))
_sym_db.RegisterMessage(Attempt)

FeatureRowExtended = _reflection.GeneratedProtocolMessageType('FeatureRowExtended', (_message.Message,), dict(
  DESCRIPTOR = _FEATUREROWEXTENDED,
  __module__ = 'feast.types.FeatureRowExtended_pb2'
  # @@protoc_insertion_point(class_scope:feast.types.FeatureRowExtended)
  ))
_sym_db.RegisterMessage(FeatureRowExtended)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
