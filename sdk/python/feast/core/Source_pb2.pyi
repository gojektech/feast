# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
builtin___str = str


class SourceType(builtin___int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: builtin___int) -> builtin___str: ...
    @classmethod
    def Value(cls, name: builtin___str) -> 'SourceType': ...
    @classmethod
    def keys(cls) -> typing___List[builtin___str]: ...
    @classmethod
    def values(cls) -> typing___List['SourceType']: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[builtin___str, 'SourceType']]: ...
    INVALID = typing___cast('SourceType', 0)
    KAFKA = typing___cast('SourceType', 1)
INVALID = typing___cast('SourceType', 0)
KAFKA = typing___cast('SourceType', 1)

class Source(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: SourceType

    @property
    def kafka_source_config(self) -> KafkaSourceConfig: ...

    def __init__(self,
        *,
        type : typing___Optional[SourceType] = None,
        kafka_source_config : typing___Optional[KafkaSourceConfig] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> Source: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"kafka_source_config",u"source_config"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"kafka_source_config",u"source_config",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"kafka_source_config",b"kafka_source_config",u"source_config",b"source_config"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"kafka_source_config",b"kafka_source_config",u"source_config",b"source_config",u"type",b"type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"source_config",b"source_config"]) -> typing_extensions___Literal["kafka_source_config"]: ...

class KafkaSourceConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    bootstrap_servers = ... # type: typing___Text
    topic = ... # type: typing___Text

    def __init__(self,
        *,
        bootstrap_servers : typing___Optional[typing___Text] = None,
        topic : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> KafkaSourceConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"bootstrap_servers",u"topic"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"bootstrap_servers",b"bootstrap_servers",u"topic",b"topic"]) -> None: ...
