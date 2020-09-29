package feast.ingestion.stores.redis


case class SparkRedisConfig(
                             namespace: String,
                             projectName: String,
                             entityColumns: Array[String],
                             timestampColumn: String,
                             iteratorGroupingSize: Int = 1000,
                             timestampPrefix: String = "_ts",
                             repartitionByEntity: Boolean = true
                           )

object SparkRedisConfig {
  val NAMESPACE = "namespace"
  val ENTITY_COLUMNS = "entity_columns"
  val TS_COLUMN = "timestamp_column"
  val ENTITY_REPARTITION = "entity_repartition"
  val PROJECT_NAME = "project_name"

  def parse(parameters: Map[String, String]): SparkRedisConfig =
    SparkRedisConfig(
      namespace = parameters.getOrElse(NAMESPACE, ""),
      projectName = parameters.getOrElse(PROJECT_NAME, "default"),
      entityColumns = parameters.getOrElse(ENTITY_COLUMNS, "").split(","),
      timestampColumn = parameters.getOrElse(TS_COLUMN, "event_timestamp"),
      repartitionByEntity = parameters.getOrElse(ENTITY_REPARTITION, "true") == "true"
    )
}
