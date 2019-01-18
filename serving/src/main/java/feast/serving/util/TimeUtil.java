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

package feast.serving.util;

import feast.serving.ServingAPIProto.TimestampRange;

/** Utility class for time-related function. */
public class TimeUtil {
  public static final int NANO_IN_MILLI = 1000000;
  public static final int NANO_IN_MICRO = 1000;
  public static final int MILLI_IN_SECOND = 1000;

  private TimeUtil() {}

  public static boolean isTimeFilterRequired(TimestampRange timeRange) {
    return timeRange != null && !TimestampRange.getDefaultInstance().equals(timeRange);
  }

  /**
   * Returns the current value of the running Java Virtual Machine's high-resolution time source, in
   * microseconds.
   *
   * @return current micro time.
   * @see System#nanoTime()
   */
  public static long microTime() {
    return System.nanoTime() / NANO_IN_MICRO;
  }
}
