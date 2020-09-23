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
package feast.core.validators;

import static feast.core.validators.Matchers.checkValidCharacters;

import feast.proto.core.EntityProto;

public class EntityValidator {
  public static void validateSpec(EntityProto.Entity entity) {
    if (entity.getSpec().getName().isEmpty()) {
      throw new IllegalArgumentException("Entity name must be provided");
    }
    if (entity.getSpec().getColumnsMap().containsKey("")) {
      throw new IllegalArgumentException("Entity columns keys must not be empty");
    }
    if (entity.getSpec().getLabelsMap().containsKey("")) {
      throw new IllegalArgumentException("Entity label keys must not be empty");
    }

    checkValidCharacters(entity.getSpec().getName(), "entity");
  }
}