/*
 * SPDX-License-Identifier: Apache-2.0
 * Copyright 2018-2019 The Feast Authors
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
package feast.core.job.databricks;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.core.IsEqual.equalTo;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;
import static org.mockito.MockitoAnnotations.initMocks;

import com.google.api.Http;
import com.google.common.collect.Lists;
import com.google.api.services.dataflow.Dataflow;
import feast.core.FeatureSetProto;
import feast.core.SourceProto;
import feast.core.StoreProto;
import feast.core.config.FeastProperties.MetricsProperties;
import feast.core.job.databricks.DatabricksJobManager;

import java.io.IOException;
import java.net.http.HttpClient;
import java.net.http.HttpResponse;
import java.util.HashMap;
import java.util.Map;

import feast.core.model.*;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.rules.ExpectedException;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.internal.util.reflection.FieldSetter;

public class DatabricksJobManagerTest {

    @Rule
    public final ExpectedException expectedException = ExpectedException.none();

    @Mock
    private Job job;

    @Mock
    private HttpClient httpClient;

    private Map<String, String> runnerConfigOptions;
    private DatabricksJobManager dbJobManager;
    private String token;

    @Before
    public void setUp() {
        initMocks(this);
        runnerConfigOptions = new HashMap<>();
        runnerConfigOptions.put("databricksHost", "https://databricks");
        token = "TEST_TOKEN";
        MetricsProperties metricsProperties = new MetricsProperties();
        metricsProperties.setEnabled(false);
        dbJobManager = new DatabricksJobManager(runnerConfigOptions, metricsProperties, token, httpClient);
        dbJobManager = spy(dbJobManager);
    }

    @Test
    public void testGetCalltoDatabricks() throws NoSuchFieldException {
//        FieldSetter.setField(job, job.getClass().getDeclaredField("extId"), "1");
        Mockito.when(job.getExtId()).thenReturn("1");

        dbJobManager.getJobStatus(job);
    }

    @Test
    public void testStartJob() throws IOException, InterruptedException {
        StoreProto.Store store =
                StoreProto.Store.newBuilder()
                        .setName("SERVING")
                        .setType(StoreProto.Store.StoreType.REDIS)
                        .setRedisConfig(StoreProto.Store.RedisConfig.newBuilder().setHost("localhost").setPort(6379).build())
                        .addSubscriptions(
                                StoreProto.Store.Subscription.newBuilder().setProject("*").setName("*").setVersion("*").build())
                        .build();

        SourceProto.Source source =
                SourceProto.Source.newBuilder()
                        .setType(SourceProto.SourceType.KAFKA)
                        .setKafkaSourceConfig(
                                SourceProto.KafkaSourceConfig.newBuilder()
                                        .setTopic("topic")
                                        .setBootstrapServers("servers:9092")
                                        .build())
                        .build();

        FeatureSetProto.FeatureSet featureSet =
                FeatureSetProto.FeatureSet.newBuilder()
                        .setSpec(
                                FeatureSetProto.FeatureSetSpec.newBuilder()
                                        .setName("featureSet")
                                        .setVersion(1)
                                        .setSource(source)
                                        .build())
                        .build();


        HttpResponse httpResponse = mock(HttpResponse.class);
        String responseBody = "{ \"run_id\" : \"1\" } ";
        when(httpResponse.body()).thenReturn(responseBody);
        when(httpResponse.statusCode()).thenReturn(200);

        Mockito.when(httpClient.send(any(), any())).thenReturn(httpResponse);

        HttpClient mockHttpClient = Mockito.mock(HttpClient.class);

        MetricsProperties metricsProperties = new MetricsProperties();
        metricsProperties.setEnabled(false);

        dbJobManager = new DatabricksJobManager(runnerConfigOptions, metricsProperties, token, httpClient);
        dbJobManager = spy(dbJobManager);

        doReturn(httpResponse).when(mockHttpClient).send(any(), any());

        Job job = new Job("3", "", "Databricks", Source.fromProto(source), Store.fromProto(store), Lists.newArrayList(FeatureSet.fromProto(featureSet)), JobStatus.PENDING);
        Job actual = dbJobManager.startJob(job);

        assertThat( actual.getExtId(), equalTo("1"));
        assertThat( actual.getId(), equalTo(job.getId()));

    }
}
