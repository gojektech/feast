# Copyright 2020 The Feast Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import enum
from typing import Dict, Optional

from feast.core.DataSource_pb2 import DataSource as DataSourceProto


class SourceType(enum.Enum):
    """
    DataSource value type. Used to define source types in DataSource.
    """

    UNKNOWN = 0
    BATCH_FILE = 1
    BATCH_BIGQUERY = 2
    STREAM_KAFKA = 3
    STREAM_KINESIS = 4


class FileOptions:
    """
    DataSource File options used to source features from a file
    """

    def __init__(
        self, file_format: str, file_url: str,
    ):
        self._file_format = file_format
        self._file_url = file_url

    @property
    def file_format(self):
        """
        Returns the file format of this file
        """
        return self._file_format

    @file_format.setter
    def file_format(self, file_format):
        """
        Sets the file format of this file
        """
        self._file_format = file_format

    @property
    def file_url(self):
        """
        Returns the file url of this file
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """
        Sets the file url of this file
        """
        self._file_url = file_url

    @classmethod
    def from_proto(cls, file_options_proto: DataSourceProto.FileOptions):
        """
        Creates a FileOptions from a protobuf representation of a file option

        Args:
            file_options_proto: A protobuf representation of a DataSource

        Returns:
            Returns a FileOptions object based on the file_options protobuf
        """

        file_options = cls(
            file_format=file_options_proto.file_format,
            file_url=file_options_proto.file_url,
        )

        return file_options

    def to_proto(self) -> DataSourceProto.FileOptions:
        """
        Converts an FileOptionsProto object to its protobuf representation.

        Returns:
            FileOptionsProto protobuf
        """

        file_options_proto = DataSourceProto.FileOptions(
            file_format=self.file_format, file_url=self.file_url,
        )

        return file_options_proto


class BigQueryOptions:
    """
    DataSource BigQuery options used to source features from BigQuery query
    """

    def __init__(
        self, table_ref: str,
    ):
        self._table_ref = table_ref

    @property
    def table_ref(self):
        """
        Returns the table ref of this BQ table
        """
        return self._table_ref

    @table_ref.setter
    def table_ref(self, table_ref):
        """
        Sets the table ref of this BQ table
        """
        self._table_ref = table_ref

    @classmethod
    def from_proto(cls, bigquery_options_proto: DataSourceProto.BigQueryOptions):
        """
        Creates a BigQueryOptions from a protobuf representation of a BigQuery option

        Args:
            bigquery_options_proto: A protobuf representation of a DataSource

        Returns:
            Returns a BigQueryOptions object based on the bigquery_options protobuf
        """

        bigquery_options = cls(table_ref=bigquery_options_proto.table_ref,)

        return bigquery_options

    def to_proto(self) -> DataSourceProto.BigQueryOptions:
        """
        Converts an BigQueryOptionsProto object to its protobuf representation.

        Returns:
            BigQueryOptionsProto protobuf
        """

        bigquery_options_proto = DataSourceProto.BigQueryOptions(
            table_ref=self.table_ref,
        )

        return bigquery_options_proto


class KafkaOptions:
    """
    DataSource Kafka options used to source features from Kafka messages
    """

    def __init__(
        self, bootstrap_servers: str, class_path: str, topic: str,
    ):
        self._bootstrap_servers = bootstrap_servers
        self._class_path = class_path
        self._topic = topic

    @property
    def bootstrap_servers(self):
        """
        Returns a comma-separated list of Kafka bootstrap servers
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """
        Sets a comma-separated list of Kafka bootstrap servers
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def class_path(self):
        """
        Returns the class path to the generated Java Protobuf class that can be
        used to decode feature data from the obtained Kafka message
        """
        return self._class_path

    @class_path.setter
    def class_path(self, class_path):
        """
        Sets the class path to the generated Java Protobuf class that can be
        used to decode feature data from the obtained Kafka message
        """
        self._class_path = class_path

    @property
    def topic(self):
        """
        Returns the Kafka topic to collect feature data from
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """
        Sets the Kafka topic to collect feature data from
        """
        self._topic = topic

    @classmethod
    def from_proto(cls, kafka_options_proto: DataSourceProto.KafkaOptions):
        """
        Creates a KafkaOptions from a protobuf representation of a kafka option

        Args:
            kafka_options_proto: A protobuf representation of a DataSource

        Returns:
            Returns a BigQueryOptions object based on the kafka_options protobuf
        """

        kafka_options = cls(
            bootstrap_servers=kafka_options_proto.bootstrap_servers,
            class_path=kafka_options_proto.class_path,
            topic=kafka_options_proto.topic,
        )

        return kafka_options

    def to_proto(self) -> DataSourceProto.KafkaOptions:
        """
        Converts an KafkaOptionsProto object to its protobuf representation.

        Returns:
            KafkaOptionsProto protobuf
        """

        kafka_options_proto = DataSourceProto.KafkaOptions(
            bootstrap_servers=self.bootstrap_servers,
            class_path=self.class_path,
            topic=self.topic,
        )

        return kafka_options_proto


class KinesisOptions:
    """
    DataSource Kinesis options used to source features from Kinesis records
    """

    def __init__(
        self, class_path: str, region: str, stream_name: str,
    ):
        self._class_path = class_path
        self._region = region
        self._stream_name = stream_name

    @property
    def class_path(self):
        """
        Returns the class path to the generated Java Protobuf class that can be
        used to decode feature data from the obtained Kinesis record
        """
        return self._class_path

    @class_path.setter
    def class_path(self, class_path):
        """
        Sets the class path to the generated Java Protobuf class that can be
        used to decode feature data from the obtained Kinesis record
        """
        self._class_path = class_path

    @property
    def region(self):
        """
        Returns the AWS region of Kinesis stream
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the AWS region of Kinesis stream
        """
        self._region = region

    @property
    def stream_name(self):
        """
        Returns the Kinesis stream name to obtain feature data from
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        """
        Sets the Kinesis stream name to obtain feature data from
        """
        self._stream_name = stream_name

    @classmethod
    def from_proto(cls, kinesis_options_proto: DataSourceProto.KinesisOptions):
        """
        Creates a KinesisOptions from a protobuf representation of a kinesis option

        Args:
            kinesis_options_proto: A protobuf representation of a DataSource

        Returns:
            Returns a KinesisOptions object based on the kinesis_options protobuf
        """

        kinesis_options = cls(
            class_path=kinesis_options_proto.class_path,
            region=kinesis_options_proto.region,
            stream_name=kinesis_options_proto.stream_name,
        )

        return kinesis_options

    def to_proto(self) -> DataSourceProto.KinesisOptions:
        """
        Converts an KinesisOptionsProto object to its protobuf representation.

        Returns:
            KinesisOptionsProto protobuf
        """

        kinesis_options_proto = DataSourceProto.KinesisOptions(
            class_path=self.class_path,
            region=self.region,
            stream_name=self.stream_name,
        )

        return kinesis_options_proto


class DataSource:
    """
    DataSource that can be used source features
    """

    def __init__(
        self,
        timestamp_column: str,
        field_mapping: Optional[Dict[str, str]] = dict(),
        date_partition_column: Optional[str] = "",
    ):
        self._timestamp_column = timestamp_column
        self._field_mapping = field_mapping
        self._date_partition_column = date_partition_column

    def __eq__(self, other):
        if not isinstance(other, DataSource):
            raise TypeError("Comparisons should only involve DataSource class objects.")

        if (
            self.timestamp_column != other.timestamp_column
            or self.field_mapping != other.field_mapping
            or self.date_partition_column != other.date_partition_column
        ):
            return False

        return True

    @property
    def field_mapping(self):
        """
        Returns the field mapping of this data source
        """
        return self._field_mapping

    @field_mapping.setter
    def field_mapping(self, field_mapping):
        """
        Sets the field mapping of this data source
        """
        self._field_mapping = field_mapping

    @property
    def timestamp_column(self):
        """
        Returns the timestamp column of this data source
        """
        return self._timestamp_column

    @timestamp_column.setter
    def timestamp_column(self, timestamp_column):
        """
        Sets the timestamp column of this data source
        """
        self._timestamp_column = timestamp_column

    @property
    def date_partition_column(self):
        """
        Returns the date partition column of this data source
        """
        return self._date_partition_column

    @date_partition_column.setter
    def date_partition_column(self, date_partition_column):
        """
        Sets the date partition column of this data source
        """
        self._date_partition_column = date_partition_column

    @staticmethod
    def from_proto(data_source):
        """
        Convert data source config in FeatureTable spec to a DataSource class object.
        """

        if data_source.file_options.file_format and data_source.file_options.file_url:
            data_source_obj = FileSource(
                field_mapping=data_source.field_mapping,
                file_format=data_source.file_options.file_format,
                file_url=data_source.file_options.file_url,
                timestamp_column=data_source.timestamp_column,
                date_partition_column=data_source.date_partition_column,
            )
        elif data_source.bigquery_options.table_ref:
            data_source_obj = BigQuerySource(
                field_mapping=data_source.field_mapping,
                table_ref=data_source.bigquery_options.table_ref,
                timestamp_column=data_source.timestamp_column,
                date_partition_column=data_source.date_partition_column,
            )
        elif (
            data_source.kafka_options.bootstrap_servers
            and data_source.kafka_options.topic
            and data_source.kafka_options.class_path
        ):
            data_source_obj = KafkaSource(
                field_mapping=data_source.field_mapping,
                bootstrap_servers=data_source.kafka_options.bootstrap_servers,
                class_path=data_source.kafka_options.class_path,
                topic=data_source.kafka_options.topic,
                timestamp_column=data_source.timestamp_column,
                date_partition_column=data_source.date_partition_column,
            )
        elif (
            data_source.kinesis_options.class_path
            and data_source.kinesis_options.region
            and data_source.kinesis_options.stream_name
        ):
            data_source_obj = KinesisSource(
                field_mapping=data_source.field_mapping,
                class_path=data_source.kinesis_options.class_path,
                region=data_source.kinesis_options.region,
                stream_name=data_source.kinesis_options.stream_name,
                timestamp_column=data_source.timestamp_column,
                date_partition_column=data_source.date_partition_column,
            )
        else:
            raise ValueError("Could not identify the source type being added")

        return data_source_obj

    def to_proto(self) -> DataSourceProto:
        """
        Converts an DataSourceProto object to its protobuf representation.
        """
        raise NotImplementedError


class FileSource(DataSource):
    def __init__(
        self,
        timestamp_column: str,
        file_format: str,
        file_url: str,
        field_mapping: Optional[Dict[str, str]] = dict(),
        date_partition_column: Optional[str] = "",
    ):
        super().__init__(timestamp_column, field_mapping, date_partition_column)
        self._file_options = FileOptions(file_format=file_format, file_url=file_url)

    def __eq__(self, other):
        if not isinstance(other, FileSource):
            raise TypeError("Comparisons should only involve FileSource class objects.")

        if (
            self.file_options.file_url != other.file_options.file_url
            or self.file_options.file_format != other.file_options.file_format
        ):
            return False

        return True

    @property
    def file_options(self):
        """
        Returns the file options of this data source
        """
        return self._file_options

    @file_options.setter
    def file_options(self, file_options):
        """
        Sets the file options of this data source
        """
        self._file_options = file_options

    @classmethod
    def from_proto(cls, data_source_proto):

        data_source = cls(
            field_mapping=data_source_proto.field_mapping,
            file_options=cls.file_options,
            timestamp_column=data_source_proto.timestamp_column,
            date_partition_column=data_source_proto.date_partition_column,
        )

        return data_source

    def to_proto(self) -> DataSourceProto:
        data_source_proto = DataSourceProto(
            type=DataSourceProto.BATCH_FILE,
            field_mapping=self.field_mapping,
            file_options=self.file_options.to_proto(),
        )

        data_source_proto.timestamp_column = self.timestamp_column
        data_source_proto.date_partition_column = self.date_partition_column

        return data_source_proto


class BigQuerySource(DataSource):
    def __init__(
        self,
        timestamp_column: str,
        table_ref: str,
        field_mapping: Optional[Dict[str, str]] = dict(),
        date_partition_column: Optional[str] = "",
    ):
        super().__init__(timestamp_column, field_mapping, date_partition_column)
        self._bigquery_options = BigQueryOptions(table_ref=table_ref,)

    def __eq__(self, other):
        if not isinstance(other, BigQuerySource):
            raise TypeError(
                "Comparisons should only involve BigQuerySource class objects."
            )

        if self.bigquery_options.table_ref != other.bigquery_options.table_ref:
            return False

        return True

    @property
    def bigquery_options(self):
        """
        Returns the bigquery options of this data source
        """
        return self._bigquery_options

    @bigquery_options.setter
    def bigquery_options(self, bigquery_options):
        """
        Sets the bigquery options of this data source
        """
        self._bigquery_options = bigquery_options

    @classmethod
    def from_proto(cls, data_source_proto):

        data_source = cls(
            field_mapping=data_source_proto.field_mapping,
            bigquery_options=cls.bigquery_options,
            timestamp_column=data_source_proto.timestamp_column,
            date_partition_column=data_source_proto.date_partition_column,
        )

        return data_source

    def to_proto(self) -> DataSourceProto:
        data_source_proto = DataSourceProto(
            type=DataSourceProto.BATCH_BIGQUERY,
            field_mapping=self.field_mapping,
            bigquery_options=self.bigquery_options.to_proto(),
        )

        data_source_proto.timestamp_column = self.timestamp_column
        data_source_proto.date_partition_column = self.date_partition_column

        return data_source_proto


class KafkaSource(DataSource):
    def __init__(
        self,
        timestamp_column: str,
        bootstrap_servers: str,
        class_path: str,
        topic: str,
        field_mapping: Optional[Dict[str, str]] = dict(),
        date_partition_column: Optional[str] = "",
    ):
        super().__init__(timestamp_column, field_mapping, date_partition_column)
        self._kafka_options = KafkaOptions(
            bootstrap_servers=bootstrap_servers, class_path=class_path, topic=topic
        )

    def __eq__(self, other):
        if not isinstance(other, KafkaSource):
            raise TypeError(
                "Comparisons should only involve KafkaSource class objects."
            )

        if (
            self.kafka_options.bootstrap_servers
            != other.kafka_options.bootstrap_servers
            or self.kafka_options.class_path != other.kafka_options.class_path
            or self.kafka_options.topic != other.kafka_options.topic
        ):
            return False

        return True

    @property
    def kafka_options(self):
        """
        Returns the kafka options of this data source
        """
        return self._kafka_options

    @kafka_options.setter
    def kafka_options(self, kafka_options):
        """
        Sets the kafka options of this data source
        """
        self._kafka_options = kafka_options

    @classmethod
    def from_proto(cls, data_source_proto):

        data_source = cls(
            field_mapping=data_source_proto.field_mapping,
            kafka_options=cls.kafka_options,
            timestamp_column=data_source_proto.timestamp_column,
            date_partition_column=data_source_proto.date_partition_column,
        )

        return data_source

    def to_proto(self) -> DataSourceProto:
        data_source_proto = DataSourceProto(
            type=DataSourceProto.STREAM_KAFKA,
            field_mapping=self.field_mapping,
            kafka_options=self.kafka_options.to_proto(),
        )

        data_source_proto.timestamp_column = self.timestamp_column
        data_source_proto.date_partition_column = self.date_partition_column

        return data_source_proto


class KinesisSource(DataSource):
    def __init__(
        self,
        timestamp_column: str,
        class_path: str,
        region: str,
        stream_name: str,
        field_mapping: Optional[Dict[str, str]] = dict(),
        date_partition_column: Optional[str] = "",
    ):
        super().__init__(timestamp_column, field_mapping, date_partition_column)
        self._kinesis_options = KinesisOptions(
            class_path=class_path, region=region, stream_name=stream_name
        )

    def __eq__(self, other):
        if not isinstance(other, KinesisSource):
            raise TypeError(
                "Comparisons should only involve KinesisSource class objects."
            )

        if (
            self.kinesis_options.class_path != other.kinesis_options.class_path
            or self.kinesis_options.region != other.kinesis_options.region
            or self.kinesis_options.stream_name != other.kinesis_options.stream_name
        ):
            return False

        return True

    @property
    def kinesis_options(self):
        """
        Returns the kinesis options of this data source
        """
        return self._kinesis_options

    @kinesis_options.setter
    def kinesis_options(self, kinesis_options):
        """
        Sets the kinesis options of this data source
        """
        self._kinesis_options = kinesis_options

    @classmethod
    def from_proto(cls, data_source_proto):

        data_source = cls(
            field_mapping=data_source_proto.field_mapping,
            kinesis_options=cls.kinesis_options,
            timestamp_column=data_source_proto.timestamp_column,
            date_partition_column=data_source_proto.date_partition_column,
        )

        return data_source

    def to_proto(self) -> DataSourceProto:
        data_source_proto = DataSourceProto(
            type=DataSourceProto.STREAM_KINESIS,
            field_mapping=self.field_mapping,
            kinesis_options=self.kinesis_options.to_proto(),
        )

        data_source_proto.timestamp_column = self.timestamp_column
        data_source_proto.date_partition_column = self.date_partition_column

        return data_source_proto
