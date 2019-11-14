# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from feast.types.Value_pb2 import (
    Value as feast___types___Value_pb2___Value,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.duration_pb2 import (
    Duration as google___protobuf___duration_pb2___Duration,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.timestamp_pb2 import (
    Timestamp as google___protobuf___timestamp_pb2___Timestamp,
)

from typing import (
    Iterable as typing___Iterable,
    List as typing___List,
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
    Tuple as typing___Tuple,
    cast as typing___cast,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class FeastServingType(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> FeastServingType: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[FeastServingType]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, FeastServingType]]: ...
    FEAST_SERVING_TYPE_INVALID = typing___cast(FeastServingType, 0)
    FEAST_SERVING_TYPE_ONLINE = typing___cast(FeastServingType, 1)
    FEAST_SERVING_TYPE_BATCH = typing___cast(FeastServingType, 2)
FEAST_SERVING_TYPE_INVALID = typing___cast(FeastServingType, 0)
FEAST_SERVING_TYPE_ONLINE = typing___cast(FeastServingType, 1)
FEAST_SERVING_TYPE_BATCH = typing___cast(FeastServingType, 2)

class JobType(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> JobType: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[JobType]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, JobType]]: ...
    JOB_TYPE_INVALID = typing___cast(JobType, 0)
    JOB_TYPE_DOWNLOAD = typing___cast(JobType, 1)
JOB_TYPE_INVALID = typing___cast(JobType, 0)
JOB_TYPE_DOWNLOAD = typing___cast(JobType, 1)

class JobStatus(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> JobStatus: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[JobStatus]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, JobStatus]]: ...
    JOB_STATUS_INVALID = typing___cast(JobStatus, 0)
    JOB_STATUS_PENDING = typing___cast(JobStatus, 1)
    JOB_STATUS_RUNNING = typing___cast(JobStatus, 2)
    JOB_STATUS_DONE = typing___cast(JobStatus, 3)
JOB_STATUS_INVALID = typing___cast(JobStatus, 0)
JOB_STATUS_PENDING = typing___cast(JobStatus, 1)
JOB_STATUS_RUNNING = typing___cast(JobStatus, 2)
JOB_STATUS_DONE = typing___cast(JobStatus, 3)

class DataFormat(int):
    DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
    @classmethod
    def Name(cls, number: int) -> str: ...
    @classmethod
    def Value(cls, name: str) -> DataFormat: ...
    @classmethod
    def keys(cls) -> typing___List[str]: ...
    @classmethod
    def values(cls) -> typing___List[DataFormat]: ...
    @classmethod
    def items(cls) -> typing___List[typing___Tuple[str, DataFormat]]: ...
    DATA_FORMAT_INVALID = typing___cast(DataFormat, 0)
    DATA_FORMAT_AVRO = typing___cast(DataFormat, 1)
DATA_FORMAT_INVALID = typing___cast(DataFormat, 0)
DATA_FORMAT_AVRO = typing___cast(DataFormat, 1)

class GetFeastServingInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeastServingInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

class GetFeastServingInfoResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    version = ... # type: typing___Text
    type = ... # type: FeastServingType
    job_staging_location = ... # type: typing___Text

    def __init__(self,
        *,
        version : typing___Optional[typing___Text] = None,
        type : typing___Optional[FeastServingType] = None,
        job_staging_location : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetFeastServingInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"job_staging_location",u"type",u"version"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"job_staging_location",b"job_staging_location",u"type",b"type",u"version",b"version"]) -> None: ...

class FeatureSetRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    version = ... # type: int
    feature_names = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def max_age(self) -> google___protobuf___duration_pb2___Duration: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        version : typing___Optional[int] = None,
        feature_names : typing___Optional[typing___Iterable[typing___Text]] = None,
        max_age : typing___Optional[google___protobuf___duration_pb2___Duration] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> FeatureSetRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"max_age"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_names",u"max_age",u"name",u"version"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"max_age",b"max_age"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"feature_names",b"feature_names",u"max_age",b"max_age",u"name",b"name",u"version",b"version"]) -> None: ...

class GetOnlineFeaturesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class EntityRow(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class FieldsEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key = ... # type: typing___Text

            @property
            def value(self) -> feast___types___Value_pb2___Value: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[feast___types___Value_pb2___Value] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> GetOnlineFeaturesRequest.EntityRow.FieldsEntry: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
            else:
                def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


        @property
        def entity_timestamp(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

        @property
        def fields(self) -> typing___MutableMapping[typing___Text, feast___types___Value_pb2___Value]: ...

        def __init__(self,
            *,
            entity_timestamp : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
            fields : typing___Optional[typing___Mapping[typing___Text, feast___types___Value_pb2___Value]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> GetOnlineFeaturesRequest.EntityRow: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"entity_timestamp"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"entity_timestamp",u"fields"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"entity_timestamp",b"entity_timestamp"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"entity_timestamp",b"entity_timestamp",u"fields",b"fields"]) -> None: ...

    omit_entities_in_response = ... # type: bool

    @property
    def feature_sets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FeatureSetRequest]: ...

    @property
    def entity_rows(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetOnlineFeaturesRequest.EntityRow]: ...

    def __init__(self,
        *,
        feature_sets : typing___Optional[typing___Iterable[FeatureSetRequest]] = None,
        entity_rows : typing___Optional[typing___Iterable[GetOnlineFeaturesRequest.EntityRow]] = None,
        omit_entities_in_response : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetOnlineFeaturesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"entity_rows",u"feature_sets",u"omit_entities_in_response"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"entity_rows",b"entity_rows",u"feature_sets",b"feature_sets",u"omit_entities_in_response",b"omit_entities_in_response"]) -> None: ...

class GetBatchFeaturesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def feature_sets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[FeatureSetRequest]: ...

    @property
    def dataset_source(self) -> DatasetSource: ...

    def __init__(self,
        *,
        feature_sets : typing___Optional[typing___Iterable[FeatureSetRequest]] = None,
        dataset_source : typing___Optional[DatasetSource] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetBatchFeaturesRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"dataset_source"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dataset_source",u"feature_sets"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"dataset_source",b"dataset_source"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dataset_source",b"dataset_source",u"feature_sets",b"feature_sets"]) -> None: ...

class GetOnlineFeaturesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FieldValues(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class FieldsEntry(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key = ... # type: typing___Text

            @property
            def value(self) -> feast___types___Value_pb2___Value: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[feast___types___Value_pb2___Value] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> GetOnlineFeaturesResponse.FieldValues.FieldsEntry: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def HasField(self, field_name: typing_extensions___Literal[u"value"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
            else:
                def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...


        @property
        def fields(self) -> typing___MutableMapping[typing___Text, feast___types___Value_pb2___Value]: ...

        def __init__(self,
            *,
            fields : typing___Optional[typing___Mapping[typing___Text, feast___types___Value_pb2___Value]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> GetOnlineFeaturesResponse.FieldValues: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"fields"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"fields",b"fields"]) -> None: ...


    @property
    def field_values(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetOnlineFeaturesResponse.FieldValues]: ...

    def __init__(self,
        *,
        field_values : typing___Optional[typing___Iterable[GetOnlineFeaturesResponse.FieldValues]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetOnlineFeaturesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"field_values"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"field_values",b"field_values"]) -> None: ...

class GetBatchFeaturesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def job(self) -> Job: ...

    def __init__(self,
        *,
        job : typing___Optional[Job] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetBatchFeaturesResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> None: ...

class GetJobRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def job(self) -> Job: ...

    def __init__(self,
        *,
        job : typing___Optional[Job] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetJobRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> None: ...

class GetJobResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def job(self) -> Job: ...

    def __init__(self,
        *,
        job : typing___Optional[Job] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetJobResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> None: ...

class Job(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    type = ... # type: JobType
    status = ... # type: JobStatus
    error = ... # type: typing___Text
    file_uris = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    data_format = ... # type: DataFormat

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        type : typing___Optional[JobType] = None,
        status : typing___Optional[JobStatus] = None,
        error : typing___Optional[typing___Text] = None,
        file_uris : typing___Optional[typing___Iterable[typing___Text]] = None,
        data_format : typing___Optional[DataFormat] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> Job: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"data_format",u"error",u"file_uris",u"id",u"status",u"type"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"data_format",b"data_format",u"error",b"error",u"file_uris",b"file_uris",u"id",b"id",u"status",b"status",u"type",b"type"]) -> None: ...

class DatasetSource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FileSource(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        file_uris = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        data_format = ... # type: DataFormat

        def __init__(self,
            *,
            file_uris : typing___Optional[typing___Iterable[typing___Text]] = None,
            data_format : typing___Optional[DataFormat] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DatasetSource.FileSource: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"data_format",u"file_uris"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"data_format",b"data_format",u"file_uris",b"file_uris"]) -> None: ...


    @property
    def file_source(self) -> DatasetSource.FileSource: ...

    def __init__(self,
        *,
        file_source : typing___Optional[DatasetSource.FileSource] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DatasetSource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"dataset_source",u"file_source"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dataset_source",u"file_source"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"dataset_source",b"dataset_source",u"file_source",b"file_source"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dataset_source",b"dataset_source",u"file_source",b"file_source"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"dataset_source",b"dataset_source"]) -> typing_extensions___Literal["file_source"]: ...
