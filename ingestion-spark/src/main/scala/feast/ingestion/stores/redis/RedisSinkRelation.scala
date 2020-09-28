package feast.ingestion.stores.redis

import com.google.protobuf.Timestamp
import com.redislabs.provider.redis.{ReadWriteConfig, RedisConfig, RedisEndpoint}
import com.redislabs.provider.redis.rdd.Keys.groupKeysByNode
import com.redislabs.provider.redis.util.PipelineUtils.{foreachWithPipeline, mapWithPipeline}
import org.apache.spark.SparkEnv
import org.apache.spark.metrics.source.RedisSinkMetricSource
import org.apache.spark.sql.sources.{BaseRelation, InsertableRelation}
import org.apache.spark.sql.types.StructType
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.{DataFrame, Row, SQLContext}


class RedisSinkRelation(override val sqlContext: SQLContext,
                        config: SparkRedisConfig) extends BaseRelation
  with InsertableRelation with Serializable {
  private implicit val redisConfig: RedisConfig = {
    new RedisConfig(
      new RedisEndpoint(sqlContext.sparkContext.getConf)
    )
  }

  private implicit val readWriteConfig: ReadWriteConfig = {
    ReadWriteConfig.fromSparkConf(sqlContext.sparkContext.getConf)
  }

  override def schema: StructType = ???

  val persistence = new HashTypePersistence(config)

  override def insert(data: DataFrame, overwrite: Boolean): Unit = {
    val dataToStore =
      if (config.repartitionByEntity)
        data.repartition(config.entityColumns.map(col): _*)
      else data

    dataToStore.foreachPartition { partition: Iterator[Row] =>
      // grouped iterator to only allocate memory for a portion of rows
      partition.grouped(config.iteratorGroupingSize).foreach { batch =>
        val rowsWithKey: Map[String, Row] = compactRowsToLatest(batch.map(row => dataKeyId(row) -> row)).toMap

        groupKeysByNode(redisConfig.hosts, rowsWithKey.keysIterator).foreach { case (node, keys) =>
          val conn = node.connect()
          val timestamps = mapWithPipeline(conn, keys) { (pipeline, key) =>
            persistence.getTimestamp(pipeline, key, timestampField)
          }

          val timestampByKey = timestamps
            .map(_.asInstanceOf[Array[Byte]])
            .map(Option(_).map(Timestamp.parseFrom).map(t => new java.sql.Timestamp(t.getSeconds * 1000)))
            .zip(rowsWithKey.keys)
            .map(_.swap)
            .toMap

          foreachWithPipeline(conn, keys) { (pipeline, key) =>
            val row = rowsWithKey(key)

            timestampByKey(key) match {
              case Some(t) if !t.before(row.getAs[java.sql.Timestamp](config.timestampColumn)) => ()
              case _ =>
                if (metricSource.nonEmpty) {
                  metricSource.get.METRIC_TOTAL_ROWS_INSERTED.inc()
                }

                val encodedRow = persistence.encodeRow(config.entityColumns, timestampField, row)
                persistence.save(pipeline, key, encodedRow, ttl = 0)
            }
          }
          conn.close()
        }
      }
    }
  }

  private def compactRowsToLatest(rows: Seq[(String, Row)]) = rows
    .groupBy(_._1)
    .values
    .map(_.maxBy(_._2.getAs[java.sql.Timestamp](config.timestampColumn).getTime))


  private def dataKeyId(row: Row): String = {
    val entityKey = config.entityColumns.map(row.getAs[Any]).map(_.toString).mkString(":")
    val entityPrefix = config.entityColumns.sorted.mkString("_")
    s"${entityPrefix}:$entityKey"
  }

  private def timestampField: String = {
    s"${config.timestampPrefix}:${config.namespace}"
  }

  private lazy val metricSource: Option[RedisSinkMetricSource] =
    SparkEnv.get.metricsSystem.getSourcesByName("redis_sink") match {
      case Seq(head) => Some(head.asInstanceOf[RedisSinkMetricSource])
      case _ => None
    }
}