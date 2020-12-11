/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright 2018-2020 The Feast Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package feast.ingestion.stores.deadletters

import org.apache.spark.SparkEnv
import org.apache.spark.metrics.source.DeadLetterSinkMetricSource
import org.apache.spark.sql.Row

object DeadLetterMetrics {
  def incrementCount(rowIterator: Iterator[Row]) = {
    val res = rowIterator
      .map(row => {
        metricSource.get.METRIC_DEADLETTER_ROWS_INSERTED.inc()
        row
      })
    res
  }

  private lazy val metricSource: Option[DeadLetterSinkMetricSource] = {
    this.synchronized {
      if (
        SparkEnv.get.metricsSystem.getSourcesByName(DeadLetterSinkMetricSource.sourceName).isEmpty
      ) {
        SparkEnv.get.metricsSystem.registerSource(new DeadLetterSinkMetricSource)
      }
    }

    SparkEnv.get.metricsSystem.getSourcesByName(DeadLetterSinkMetricSource.sourceName) match {
      case Seq(head) => Some(head.asInstanceOf[DeadLetterSinkMetricSource])
      case _         => None
    }
  }
}
