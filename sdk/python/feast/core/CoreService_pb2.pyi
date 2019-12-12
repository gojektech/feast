# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from feast.core.FeatureSet_pb2 import (
    FeatureSetSpec as feast___core___FeatureSet_pb2___FeatureSetSpec,
)

from feast.core.Store_pb2 import (
    Store as feast___core___Store_pb2___Store,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetFeatureSetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    project = ... # type: typing___Text
    name = ... # type: typing___Text
    version = ... # type: int

    def __init__(self,
        *,
        project : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        version : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeatureSetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name",u"project",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"project",b"project",u"version",b"version"]) -> None: ...

class GetFeatureSetResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSetSpec: ...

    def __init__(self,
        *,
        feature_set : typing___Optional[feast___core___FeatureSet_pb2___FeatureSetSpec] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeatureSetResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set"]) -> None: ...

class ListFeatureSetsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Filter(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        feature_set_name = ... # type: typing___Text
        feature_set_version = ... # type: typing___Text

        def __init__(self,
            *,
            feature_set_name : typing___Optional[typing___Text] = None,
            feature_set_version : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListFeatureSetsRequest.Filter: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"feature_set_name",u"feature_set_version"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"feature_set_name",b"feature_set_name",u"feature_set_version",b"feature_set_version"]) -> None: ...

    project = ... # type: typing___Text

    @property
    def filter(self) -> ListFeatureSetsRequest.Filter: ...

    def __init__(self,
        *,
        project : typing___Optional[typing___Text] = None,
        filter : typing___Optional[ListFeatureSetsRequest.Filter] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListFeatureSetsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"filter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter",u"project"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"filter",b"filter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter",b"filter",u"project",b"project"]) -> None: ...

class ListFeatureSetsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def feature_sets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[feast___core___FeatureSet_pb2___FeatureSetSpec]: ...

    def __init__(self,
        *,
        feature_sets : typing___Optional[typing___Iterable[feast___core___FeatureSet_pb2___FeatureSetSpec]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListFeatureSetsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_sets"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_sets",b"feature_sets"]) -> None: ...

class ListStoresRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Filter(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListStoresRequest.Filter: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...


    @property
    def filter(self) -> ListStoresRequest.Filter: ...

    def __init__(self,
        *,
        filter : typing___Optional[ListStoresRequest.Filter] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListStoresRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"filter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"filter",b"filter"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter",b"filter"]) -> None: ...

class ListStoresResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def store(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[feast___core___Store_pb2___Store]: ...

    def __init__(self,
        *,
        store : typing___Optional[typing___Iterable[feast___core___Store_pb2___Store]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListStoresResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"store"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"store",b"store"]) -> None: ...

class ApplyFeatureSetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    project = ... # type: typing___Text

    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSetSpec: ...

    def __init__(self,
        *,
        project : typing___Optional[typing___Text] = None,
        feature_set : typing___Optional[feast___core___FeatureSet_pb2___FeatureSetSpec] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyFeatureSetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set",u"project"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set",u"project",b"project"]) -> None: ...

class ApplyFeatureSetResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Status(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> ApplyFeatureSetResponse.Status: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[ApplyFeatureSetResponse.Status]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, ApplyFeatureSetResponse.Status]]: ...
        NO_CHANGE = typing___cast(ApplyFeatureSetResponse.Status, 0)
        CREATED = typing___cast(ApplyFeatureSetResponse.Status, 1)
        ERROR = typing___cast(ApplyFeatureSetResponse.Status, 2)
    NO_CHANGE = typing___cast(ApplyFeatureSetResponse.Status, 0)
    CREATED = typing___cast(ApplyFeatureSetResponse.Status, 1)
    ERROR = typing___cast(ApplyFeatureSetResponse.Status, 2)

    status = ... # type: ApplyFeatureSetResponse.Status

    @property
    def feature_set(self) -> feast___core___FeatureSet_pb2___FeatureSetSpec: ...

    def __init__(self,
        *,
        feature_set : typing___Optional[feast___core___FeatureSet_pb2___FeatureSetSpec] = None,
        status : typing___Optional[ApplyFeatureSetResponse.Status] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ApplyFeatureSetResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set",u"status"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_set",b"feature_set",u"status",b"status"]) -> None: ...

class GetFeastCoreVersionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeastCoreVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class GetFeastCoreVersionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ... # type: typing___Text

    def __init__(self,
        *,
        version : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeastCoreVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"version",b"version"]) -> None: ...

class UpdateStoreRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def store(self) -> feast___core___Store_pb2___Store: ...

    def __init__(self,
        *,
        store : typing___Optional[feast___core___Store_pb2___Store] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateStoreRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"store"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"store"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"store",b"store"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"store",b"store"]) -> None: ...

class UpdateStoreResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Status(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> UpdateStoreResponse.Status: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[UpdateStoreResponse.Status]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, UpdateStoreResponse.Status]]: ...
        NO_CHANGE = typing___cast(UpdateStoreResponse.Status, 0)
        UPDATED = typing___cast(UpdateStoreResponse.Status, 1)
    NO_CHANGE = typing___cast(UpdateStoreResponse.Status, 0)
    UPDATED = typing___cast(UpdateStoreResponse.Status, 1)

    status = ... # type: UpdateStoreResponse.Status

    @property
    def store(self) -> feast___core___Store_pb2___Store: ...

    def __init__(self,
        *,
        store : typing___Optional[feast___core___Store_pb2___Store] = None,
        status : typing___Optional[UpdateStoreResponse.Status] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UpdateStoreResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"store"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"status",u"store"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"store",b"store"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"status",b"status",u"store",b"store"]) -> None: ...

class CreateProjectRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CreateProjectRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...

class CreateProjectResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CreateProjectResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ArchiveProjectRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ArchiveProjectRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"name"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name"]) -> None: ...

class ArchiveProjectResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ArchiveProjectResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ListProjectsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListProjectsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class ListProjectsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    projects = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    def __init__(self,
        *,
        projects : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListProjectsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"projects"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"projects",b"projects"]) -> None: ...
