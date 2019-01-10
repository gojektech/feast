/*
 * Copyright 2018 The Feast Authors
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
 *
 */

package feast.core.job;

import feast.core.model.JobInfo;
import feast.core.model.JobStatus;
import feast.core.model.Metrics;
import java.util.List;

public interface JobMonitor {

  /**
   * Get status of a job given runner-specific job ID.
   *
   * @param job job.
   * @return job status.
   */
  JobStatus getJobStatus(JobInfo job);

  /**
   * Get metrics of a job.
   *
   * @param job .
   * @return list of metrics associated with the job.
   */
  List<Metrics> getJobMetrics(JobInfo job);
}
