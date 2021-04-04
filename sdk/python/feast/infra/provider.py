import abc
from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

import pandas
import pyarrow

from feast.data_source import DataSource
from feast.feature_table import FeatureTable
from feast.feature_view import FeatureView
from feast.protos.feast.types.EntityKey_pb2 import EntityKey as EntityKeyProto
from feast.protos.feast.types.Value_pb2 import Value as ValueProto
from feast.repo_config import RepoConfig

ENTITY_DF_EVENT_TIMESTAMP_COL = "event_timestamp"


class RetrievalJob(abc.ABC):
    """RetrievalJob is used to manage the execution of a historical feature retrieval"""

    @abc.abstractmethod
    def to_df(self):
        """Return dataset as Pandas DataFrame synchronously"""
        pass


class Provider(abc.ABC):
    @abc.abstractmethod
    def update_infra(
        self,
        project: str,
        tables_to_delete: Sequence[Union[FeatureTable, FeatureView]],
        tables_to_keep: Sequence[Union[FeatureTable, FeatureView]],
        partial: bool,
    ):
        """
        Reconcile cloud resources with the objects declared in the feature repo.

        Args:
            project: Project to which tables belong
            tables_to_delete: Tables that were deleted from the feature repo, so provider needs to
                clean up the corresponding cloud resources.
            tables_to_keep: Tables that are still in the feature repo. Depending on implementation,
                provider may or may not need to update the corresponding resources.
            partial: if true, then tables_to_delete and tables_to_keep are *not* exhaustive lists.
                There may be other tables that are not touched by this update.
        """
        ...

    @abc.abstractmethod
    def teardown_infra(
        self, project: str, tables: Sequence[Union[FeatureTable, FeatureView]]
    ):
        """
        Tear down all cloud resources for a repo.

        Args:
            project: Feast project to which tables belong
            tables: Tables that are declared in the feature repo.
        """
        ...

    @abc.abstractmethod
    def online_write_batch(
        self,
        project: str,
        table: Union[FeatureTable, FeatureView],
        data: List[
            Tuple[EntityKeyProto, Dict[str, ValueProto], datetime, Optional[datetime]]
        ],
        progress: Optional[Callable[[int], Any]],
    ) -> None:
        """
        Write a batch of feature rows to the online store. This is a low level interface, not
        expected to be used by the users directly.

        If a tz-naive timestamp is passed to this method, it is assumed to be UTC.

        Args:
            project: Feast project name
            table: Feast FeatureTable
            data: a list of quadruplets containing Feature data. Each quadruplet contains an Entity Key,
                a dict containing feature values, an event timestamp for the row, and
                the created timestamp for the row if it exists.
            progress: Optional function to be called once every mini-batch of rows is written to
                the online store. Can be used to display progress.
        """
        ...

    @staticmethod
    @abc.abstractmethod
    def pull_latest_from_table_or_query(
        data_source: DataSource,
        entity_names: List[str],
        feature_names: List[str],
        event_timestamp_column: str,
        created_timestamp_column: Optional[str],
        start_date: datetime,
        end_date: datetime,
    ) -> pyarrow.Table:
        """
        Note that entity_names, feature_names, event_timestamp_column, and created_timestamp_column
        have all already been mapped back to column names of the source table
        and those column names are the values passed into this function.
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def get_historical_features(
        config: RepoConfig,
        feature_views: List[FeatureView],
        feature_refs: List[str],
        entity_df: Union[pandas.DataFrame, str],
    ) -> RetrievalJob:
        pass

    @abc.abstractmethod
    def online_read(
        self,
        project: str,
        table: Union[FeatureTable, FeatureView],
        entity_keys: List[EntityKeyProto],
    ) -> List[Tuple[Optional[datetime], Optional[Dict[str, ValueProto]]]]:
        """
        Read feature values given an Entity Key. This is a low level interface, not
        expected to be used by the users directly.

        Returns:
            Data is returned as a list, one item per entity key. Each item in the list is a tuple
            of event_ts for the row, and the feature data as a dict from feature names to values.
            Values are returned as Value proto message.
        """
        ...


def get_provider(config: RepoConfig) -> Provider:
    if config.provider == "gcp":
        from feast.infra.gcp import Gcp

        return Gcp(config.online_store.datastore if config.online_store else None)
    elif config.provider == "local":
        from feast.infra.local_sqlite import LocalSqlite

        assert config.online_store is not None
        assert config.online_store.local is not None
        return LocalSqlite(config.online_store.local)
    else:
        raise ValueError(config)


def _get_requested_feature_views_to_features_dict(
    feature_refs: List[str], feature_views: List[FeatureView]
) -> Dict[FeatureView, List[str]]:
    """Create a dict of FeatureView -> List[Feature] for all requested features"""

    feature_views_to_feature_map = {}  # type: Dict[FeatureView, List[str]]
    for ref in feature_refs:
        ref_parts = ref.split(":")
        feature_view_from_ref = ref_parts[0]
        feature_from_ref = ref_parts[1]
        found = False
        for feature_view_from_registry in feature_views:
            if feature_view_from_registry.name == feature_view_from_ref:
                found = True
                if feature_view_from_registry in feature_views_to_feature_map:
                    feature_views_to_feature_map[feature_view_from_registry].append(
                        feature_from_ref
                    )
                else:
                    feature_views_to_feature_map[feature_view_from_registry] = [
                        feature_from_ref
                    ]

        if not found:
            raise ValueError(f"Could not find feature view from reference {ref}")
    return feature_views_to_feature_map
