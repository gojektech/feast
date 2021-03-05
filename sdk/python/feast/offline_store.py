# Copyright 2019 The Feast Authors
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
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional
import pyarrow


class OfflineStore(ABC):
    @abstractmethod
    def pull_table(
        self,
        table_ref: str,
        event_timestamp_column: str,
        start_date: datetime,
        end_date: datetime,
    ):
        pass


class BigQueryOfflineStore:
    def pull_table(
        self,
        table_ref: str,
        event_timestamp_column: str,
        start_date: datetime,
        end_date: datetime,
    ) -> Optional[pyarrow.Table]:
        from google.cloud.bigquery_storage import BigQueryReadClient, types

        project, dataset, table = table_ref.split(".")
        client = BigQueryReadClient()

        requested_session = types.ReadSession()
        requested_session.table = f"projects/{project}/datasets/{dataset}/tables/{table}"
        requested_session.data_format = types.DataFormat.ARROW
        requested_session.read_options.row_restriction = f"{event_timestamp_column} BETWEEN TIMESTAMP('{start_date}') AND TIMESTAMP('{end_date}')"
        parent = f"projects/{project}"
        session = client.create_read_session(
            parent=parent,
            read_session=requested_session,
            max_stream_count=1,
        )
        if len(session.streams) == 0:
            # will sometimes happen, indicates no data
            return None
        reader = client.read_rows(session.streams[0].name)
        rows = reader.rows(session).to_arrow()
        return rows
