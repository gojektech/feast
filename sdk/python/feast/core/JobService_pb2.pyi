# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from feast.specs.ImportSpec_pb2 import (
    ImportSpec as feast___specs___ImportSpec_pb2___ImportSpec,
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
    Mapping as typing___Mapping,
    MutableMapping as typing___MutableMapping,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class JobServiceTypes(google___protobuf___message___Message):
    class SubmitImportJobRequest(google___protobuf___message___Message):
        name = ... # type: typing___Text

        @property
        def importSpec(self) -> feast___specs___ImportSpec_pb2___ImportSpec: ...

        def __init__(self,
            importSpec : typing___Optional[feast___specs___ImportSpec_pb2___ImportSpec] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.SubmitImportJobRequest: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"importSpec"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"importSpec",u"name"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"importSpec",b"importSpec"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"importSpec",b"name"]) -> None: ...

    class SubmitImportJobResponse(google___protobuf___message___Message):
        jobId = ... # type: typing___Text

        def __init__(self,
            jobId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.SubmitImportJobResponse: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"jobId"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"jobId"]) -> None: ...

    class ListJobsResponse(google___protobuf___message___Message):

        @property
        def jobs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[JobServiceTypes.JobDetail]: ...

        def __init__(self,
            jobs : typing___Optional[typing___Iterable[JobServiceTypes.JobDetail]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.ListJobsResponse: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"jobs"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"jobs"]) -> None: ...

    class GetJobRequest(google___protobuf___message___Message):
        id = ... # type: typing___Text

        def __init__(self,
            id : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.GetJobRequest: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

    class GetJobResponse(google___protobuf___message___Message):

        @property
        def job(self) -> JobServiceTypes.JobDetail: ...

        def __init__(self,
            job : typing___Optional[JobServiceTypes.JobDetail] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.GetJobResponse: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"job"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"job"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"job",b"job"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"job"]) -> None: ...

    class AbortJobRequest(google___protobuf___message___Message):
        id = ... # type: typing___Text

        def __init__(self,
            id : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.AbortJobRequest: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

    class AbortJobResponse(google___protobuf___message___Message):
        id = ... # type: typing___Text

        def __init__(self,
            id : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.AbortJobResponse: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"id"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"id"]) -> None: ...

    class JobDetail(google___protobuf___message___Message):
        class MetricsEntry(google___protobuf___message___Message):
            key = ... # type: typing___Text
            value = ... # type: float

            def __init__(self,
                key : typing___Optional[typing___Text] = None,
                value : typing___Optional[float] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> JobServiceTypes.JobDetail.MetricsEntry: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...

        id = ... # type: typing___Text
        extId = ... # type: typing___Text
        type = ... # type: typing___Text
        runner = ... # type: typing___Text
        status = ... # type: typing___Text
        entities = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        features = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def metrics(self) -> typing___MutableMapping[typing___Text, float]: ...

        @property
        def lastUpdated(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

        @property
        def created(self) -> google___protobuf___timestamp_pb2___Timestamp: ...

        def __init__(self,
            id : typing___Optional[typing___Text] = None,
            extId : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            runner : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            entities : typing___Optional[typing___Iterable[typing___Text]] = None,
            features : typing___Optional[typing___Iterable[typing___Text]] = None,
            metrics : typing___Optional[typing___Mapping[typing___Text, float]] = None,
            lastUpdated : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
            created : typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> JobServiceTypes.JobDetail: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"created",u"lastUpdated"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"created",u"entities",u"extId",u"features",u"id",u"lastUpdated",u"metrics",u"runner",u"status",u"type"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"created",b"created",u"lastUpdated",b"lastUpdated"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[b"created",b"entities",b"extId",b"features",b"id",b"lastUpdated",b"metrics",b"runner",b"status",b"type"]) -> None: ...


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> JobServiceTypes: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
