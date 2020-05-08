# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feast/core/Store.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='feast/core/Store.proto',
  package='feast.core',
  syntax='proto3',
  serialized_options=b'\n\nfeast.coreB\nStoreProtoZ/github.com/gojek/feast/sdk/go/protos/feast/core',
  serialized_pb=b'\n\x16\x66\x65\x61st/core/Store.proto\x12\nfeast.core\x1a\x1egoogle/protobuf/duration.proto\"0\n\x0bSetOfStores\x12!\n\x06stores\x18\x01 \x03(\x0b\x32\x11.feast.core.Store\"\xff\x07\n\x05Store\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.feast.core.Store.StoreType\x12\x35\n\rsubscriptions\x18\x04 \x03(\x0b\x32\x1e.feast.core.Store.Subscription\x12\x35\n\x0credis_config\x18\x0b \x01(\x0b\x32\x1d.feast.core.Store.RedisConfigH\x00\x12;\n\x0f\x62igquery_config\x18\x0c \x01(\x0b\x32 .feast.core.Store.BigQueryConfigH\x00\x12=\n\x10\x63\x61ssandra_config\x18\r \x01(\x0b\x32!.feast.core.Store.CassandraConfigH\x00\x12\x33\n\x0bhive_config\x18\x0e \x01(\x0b\x32\x1c.feast.core.Store.HiveConfigH\x00\x1a)\n\x0bRedisConfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x1a\x38\n\x0e\x42igQueryConfig\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x1a\xa1\x02\n\x0f\x43\x61ssandraConfig\x12\x17\n\x0f\x62ootstrap_hosts\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x10\n\x08keyspace\x18\x03 \x01(\t\x12\x12\n\ntable_name\x18\x04 \x01(\t\x12V\n\x13replication_options\x18\x05 \x03(\x0b\x32\x39.feast.core.Store.CassandraConfig.ReplicationOptionsEntry\x12.\n\x0b\x64\x65\x66\x61ult_ttl\x18\x06 \x01(\x0b\x32\x19.google.protobuf.Duration\x1a\x39\n\x17ReplicationOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x8f\x01\n\nHiveConfig\x12\x15\n\rdatabase_name\x18\x01 \x01(\t\x12:\n\x07options\x18\x02 \x03(\x0b\x32).feast.core.Store.HiveConfig.OptionsEntry\x1a.\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0cSubscription\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"J\n\tStoreType\x12\x0b\n\x07INVALID\x10\x00\x12\t\n\x05REDIS\x10\x01\x12\x0c\n\x08\x42IGQUERY\x10\x02\x12\r\n\tCASSANDRA\x10\x03\x12\x08\n\x04HIVE\x10\x04\x42\x08\n\x06\x63onfigBI\n\nfeast.coreB\nStoreProtoZ/github.com/gojek/feast/sdk/go/protos/feast/coreb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])



_STORE_STORETYPE = _descriptor.EnumDescriptor(
  name='StoreType',
  full_name='feast.core.Store.StoreType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REDIS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BIGQUERY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CASSANDRA', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIVE', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1060,
  serialized_end=1134,
)
_sym_db.RegisterEnumDescriptor(_STORE_STORETYPE)


_SETOFSTORES = _descriptor.Descriptor(
  name='SetOfStores',
  full_name='feast.core.SetOfStores',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stores', full_name='feast.core.SetOfStores.stores', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=70,
  serialized_end=118,
)


_STORE_REDISCONFIG = _descriptor.Descriptor(
  name='RedisConfig',
  full_name='feast.core.Store.RedisConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='feast.core.Store.RedisConfig.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='feast.core.Store.RedisConfig.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=474,
  serialized_end=515,
)

_STORE_BIGQUERYCONFIG = _descriptor.Descriptor(
  name='BigQueryConfig',
  full_name='feast.core.Store.BigQueryConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='feast.core.Store.BigQueryConfig.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='feast.core.Store.BigQueryConfig.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=517,
  serialized_end=573,
)

_STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY = _descriptor.Descriptor(
  name='ReplicationOptionsEntry',
  full_name='feast.core.Store.CassandraConfig.ReplicationOptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.Store.CassandraConfig.ReplicationOptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.Store.CassandraConfig.ReplicationOptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=808,
  serialized_end=865,
)

_STORE_CASSANDRACONFIG = _descriptor.Descriptor(
  name='CassandraConfig',
  full_name='feast.core.Store.CassandraConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bootstrap_hosts', full_name='feast.core.Store.CassandraConfig.bootstrap_hosts', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='feast.core.Store.CassandraConfig.port', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keyspace', full_name='feast.core.Store.CassandraConfig.keyspace', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='table_name', full_name='feast.core.Store.CassandraConfig.table_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replication_options', full_name='feast.core.Store.CassandraConfig.replication_options', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_ttl', full_name='feast.core.Store.CassandraConfig.default_ttl', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=576,
  serialized_end=865,
)

_STORE_HIVECONFIG_OPTIONSENTRY = _descriptor.Descriptor(
  name='OptionsEntry',
  full_name='feast.core.Store.HiveConfig.OptionsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='feast.core.Store.HiveConfig.OptionsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='feast.core.Store.HiveConfig.OptionsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=965,
  serialized_end=1011,
)

_STORE_HIVECONFIG = _descriptor.Descriptor(
  name='HiveConfig',
  full_name='feast.core.Store.HiveConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='database_name', full_name='feast.core.Store.HiveConfig.database_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='feast.core.Store.HiveConfig.options', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STORE_HIVECONFIG_OPTIONSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=868,
  serialized_end=1011,
)

_STORE_SUBSCRIPTION = _descriptor.Descriptor(
  name='Subscription',
  full_name='feast.core.Store.Subscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.Store.Subscription.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='feast.core.Store.Subscription.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1013,
  serialized_end=1058,
)

_STORE = _descriptor.Descriptor(
  name='Store',
  full_name='feast.core.Store',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='feast.core.Store.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='feast.core.Store.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscriptions', full_name='feast.core.Store.subscriptions', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='redis_config', full_name='feast.core.Store.redis_config', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bigquery_config', full_name='feast.core.Store.bigquery_config', index=4,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cassandra_config', full_name='feast.core.Store.cassandra_config', index=5,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hive_config', full_name='feast.core.Store.hive_config', index=6,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STORE_REDISCONFIG, _STORE_BIGQUERYCONFIG, _STORE_CASSANDRACONFIG, _STORE_HIVECONFIG, _STORE_SUBSCRIPTION, ],
  enum_types=[
    _STORE_STORETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='config', full_name='feast.core.Store.config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=121,
  serialized_end=1144,
)

_SETOFSTORES.fields_by_name['stores'].message_type = _STORE
_STORE_REDISCONFIG.containing_type = _STORE
_STORE_BIGQUERYCONFIG.containing_type = _STORE
_STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY.containing_type = _STORE_CASSANDRACONFIG
_STORE_CASSANDRACONFIG.fields_by_name['replication_options'].message_type = _STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY
_STORE_CASSANDRACONFIG.fields_by_name['default_ttl'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_STORE_CASSANDRACONFIG.containing_type = _STORE
_STORE_HIVECONFIG_OPTIONSENTRY.containing_type = _STORE_HIVECONFIG
_STORE_HIVECONFIG.fields_by_name['options'].message_type = _STORE_HIVECONFIG_OPTIONSENTRY
_STORE_HIVECONFIG.containing_type = _STORE
_STORE_SUBSCRIPTION.containing_type = _STORE
_STORE.fields_by_name['type'].enum_type = _STORE_STORETYPE
_STORE.fields_by_name['subscriptions'].message_type = _STORE_SUBSCRIPTION
_STORE.fields_by_name['redis_config'].message_type = _STORE_REDISCONFIG
_STORE.fields_by_name['bigquery_config'].message_type = _STORE_BIGQUERYCONFIG
_STORE.fields_by_name['cassandra_config'].message_type = _STORE_CASSANDRACONFIG
_STORE.fields_by_name['hive_config'].message_type = _STORE_HIVECONFIG
_STORE_STORETYPE.containing_type = _STORE
_STORE.oneofs_by_name['config'].fields.append(
  _STORE.fields_by_name['redis_config'])
_STORE.fields_by_name['redis_config'].containing_oneof = _STORE.oneofs_by_name['config']
_STORE.oneofs_by_name['config'].fields.append(
  _STORE.fields_by_name['bigquery_config'])
_STORE.fields_by_name['bigquery_config'].containing_oneof = _STORE.oneofs_by_name['config']
_STORE.oneofs_by_name['config'].fields.append(
  _STORE.fields_by_name['cassandra_config'])
_STORE.fields_by_name['cassandra_config'].containing_oneof = _STORE.oneofs_by_name['config']
_STORE.oneofs_by_name['config'].fields.append(
  _STORE.fields_by_name['hive_config'])
_STORE.fields_by_name['hive_config'].containing_oneof = _STORE.oneofs_by_name['config']
DESCRIPTOR.message_types_by_name['SetOfStores'] = _SETOFSTORES
DESCRIPTOR.message_types_by_name['Store'] = _STORE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SetOfStores = _reflection.GeneratedProtocolMessageType('SetOfStores', (_message.Message,), {
  'DESCRIPTOR' : _SETOFSTORES,
  '__module__' : 'feast.core.Store_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.SetOfStores)
  })
_sym_db.RegisterMessage(SetOfStores)

Store = _reflection.GeneratedProtocolMessageType('Store', (_message.Message,), {

  'RedisConfig' : _reflection.GeneratedProtocolMessageType('RedisConfig', (_message.Message,), {
    'DESCRIPTOR' : _STORE_REDISCONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.RedisConfig)
    })
  ,

  'BigQueryConfig' : _reflection.GeneratedProtocolMessageType('BigQueryConfig', (_message.Message,), {
    'DESCRIPTOR' : _STORE_BIGQUERYCONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.BigQueryConfig)
    })
  ,

  'CassandraConfig' : _reflection.GeneratedProtocolMessageType('CassandraConfig', (_message.Message,), {

    'ReplicationOptionsEntry' : _reflection.GeneratedProtocolMessageType('ReplicationOptionsEntry', (_message.Message,), {
      'DESCRIPTOR' : _STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY,
      '__module__' : 'feast.core.Store_pb2'
      # @@protoc_insertion_point(class_scope:feast.core.Store.CassandraConfig.ReplicationOptionsEntry)
      })
    ,
    'DESCRIPTOR' : _STORE_CASSANDRACONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.CassandraConfig)
    })
  ,

  'HiveConfig' : _reflection.GeneratedProtocolMessageType('HiveConfig', (_message.Message,), {

    'OptionsEntry' : _reflection.GeneratedProtocolMessageType('OptionsEntry', (_message.Message,), {
      'DESCRIPTOR' : _STORE_HIVECONFIG_OPTIONSENTRY,
      '__module__' : 'feast.core.Store_pb2'
      # @@protoc_insertion_point(class_scope:feast.core.Store.HiveConfig.OptionsEntry)
      })
    ,
    'DESCRIPTOR' : _STORE_HIVECONFIG,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.HiveConfig)
    })
  ,

  'Subscription' : _reflection.GeneratedProtocolMessageType('Subscription', (_message.Message,), {
    'DESCRIPTOR' : _STORE_SUBSCRIPTION,
    '__module__' : 'feast.core.Store_pb2'
    # @@protoc_insertion_point(class_scope:feast.core.Store.Subscription)
    })
  ,
  'DESCRIPTOR' : _STORE,
  '__module__' : 'feast.core.Store_pb2'
  # @@protoc_insertion_point(class_scope:feast.core.Store)
  })
_sym_db.RegisterMessage(Store)
_sym_db.RegisterMessage(Store.RedisConfig)
_sym_db.RegisterMessage(Store.BigQueryConfig)
_sym_db.RegisterMessage(Store.CassandraConfig)
_sym_db.RegisterMessage(Store.CassandraConfig.ReplicationOptionsEntry)
_sym_db.RegisterMessage(Store.HiveConfig)
_sym_db.RegisterMessage(Store.HiveConfig.OptionsEntry)
_sym_db.RegisterMessage(Store.Subscription)


DESCRIPTOR._options = None
_STORE_CASSANDRACONFIG_REPLICATIONOPTIONSENTRY._options = None
_STORE_HIVECONFIG_OPTIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
