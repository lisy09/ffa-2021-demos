# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
def get_provider_info():
    return {
        'package-name': 'apache-airflow-providers-google',
        'name': 'Google',
        'description': 'Google services including:\n\n  - `Google Ads <https://ads.google.com/>`__\n  - `Google Cloud (GCP) <https://cloud.google.com/>`__\n  - `Google Firebase <https://firebase.google.com/>`__\n  - `Google Marketing Platform <https://marketingplatform.google.com/>`__\n  - `Google Workspace <https://workspace.google.pl/>`__ (formerly Google Suite)\n',
        'versions': ['1.0.0'],
        'integrations': [
            {
                'integration-name': 'Google Analytics360',
                'external-doc-url': 'https://analytics.google.com/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/marketing_platform/analytics.rst'
                ],
                'tags': ['gmp'],
            },
            {
                'integration-name': 'Google Ads',
                'external-doc-url': 'https://ads.google.com/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/ads.rst'],
                'tags': ['gmp'],
            },
            {
                'integration-name': 'Google AutoML',
                'external-doc-url': 'https://cloud.google.com/automl/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/automl.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google BigQuery Data Transfer Service',
                'external-doc-url': 'https://cloud.google.com/bigquery/transfer/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/bigquery_dts.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google BigQuery',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/bigquery.rst'],
                'external-doc-url': 'https://cloud.google.com/bigquery/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Bigtable',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/bigtable.rst'],
                'external-doc-url': 'https://cloud.google.com/bigtable/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Build',
                'external-doc-url': 'https://cloud.google.com/cloud-build/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/cloud_build.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Data Loss Prevention (DLP)',
                'external-doc-url': 'https://cloud.google.com/dlp/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/data_loss_prevention.rst'
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Firestore',
                'external-doc-url': 'https://firebase.google.com/docs/firestore',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/firebase/firestore.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Functions',
                'external-doc-url': 'https://cloud.google.com/functions/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/functions.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Key Management Service (KMS)',
                'external-doc-url': 'https://cloud.google.com/kms/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Life Sciences',
                'external-doc-url': 'https://cloud.google.com/life-sciences/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/life_sciences.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Memorystore',
                'external-doc-url': 'https://cloud.google.com/memorystore/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/cloud_memorystore.rst',
                    '/docs/apache-airflow-providers-google/operators/cloud/cloud_memorystore_memcached.rst',
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud OS Login',
                'external-doc-url': 'https://cloud.google.com/compute/docs/oslogin/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Pub/Sub',
                'external-doc-url': 'https://cloud.google.com/pubsub/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/pubsub.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Secret Manager',
                'external-doc-url': 'https://cloud.google.com/secret-manager/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Spanner',
                'external-doc-url': 'https://cloud.google.com/spanner/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/spanner.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Speech-to-Text',
                'external-doc-url': 'https://cloud.google.com/speech-to-text/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/speech_to_text.rst',
                    '/docs/apache-airflow-providers-google/operators/cloud/translate_speech.rst',
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud SQL',
                'external-doc-url': 'https://cloud.google.com/sql/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/cloud_sql.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Stackdriver',
                'external-doc-url': 'https://cloud.google.com/stackdriver',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/stackdriver.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Storage (GCS)',
                'external-doc-url': 'https://cloud.google.com/gcs/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/gcs.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Tasks',
                'external-doc-url': 'https://cloud.google.com/tasks/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Text-to-Speech',
                'external-doc-url': 'https://cloud.google.com/text-to-speech/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/text_to_speech.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Translation',
                'external-doc-url': 'https://cloud.google.com/translate/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/translate.rst',
                    '/docs/apache-airflow-providers-google/operators/cloud/translate_speech.rst',
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Video Intelligence',
                'external-doc-url': 'https://cloud.google.com/video_intelligence/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/video_intelligence.rst'
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Vision',
                'external-doc-url': 'https://cloud.google.com/vision/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/vision.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Compute Engine',
                'external-doc-url': 'https://cloud.google.com/compute/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/compute.rst',
                    '/docs/apache-airflow-providers-google/operators/cloud/compute_ssh.rst',
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Data Proc',
                'external-doc-url': 'https://cloud.yandex.com/services/data-proc',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Data Catalog',
                'external-doc-url': 'https://cloud.google.com/data-catalog',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/datacatalog.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Dataflow',
                'external-doc-url': 'https://cloud.google.com/dataflow/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Data Fusion',
                'external-doc-url': 'https://cloud.google.com/data-fusion/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/datafusion.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Dataprep',
                'external-doc-url': 'https://cloud.google.com/dataprep/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/dataprep.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Dataproc',
                'external-doc-url': 'https://cloud.google.com/dataproc/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/dataproc.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Datastore',
                'external-doc-url': 'https://cloud.google.com/datastore/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/datastore.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Deployment Manager',
                'external-doc-url': 'https://cloud.google.com/deployment-manager/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google API Python Client',
                'external-doc-url': 'https://github.com/googleapis/google-api-python-client',
                'tags': ['google'],
            },
            {
                'integration-name': 'Google Campaign Manager',
                'external-doc-url': 'https://developers.google.com/doubleclick-advertisers',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/marketing_platform/campaign_manager.rst'
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud',
                'external-doc-url': 'https://cloud.google.com/',
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Discovery API',
                'external-doc-url': 'https://developers.google.com/discovery',
                'tags': ['google'],
            },
            {
                'integration-name': 'Google Display&Video 360',
                'external-doc-url': 'https://marketingplatform.google.com/about/display-video-360/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/marketing_platform/display_video.rst'
                ],
                'tags': ['gmp'],
            },
            {
                'integration-name': 'Google Drive',
                'external-doc-url': 'https://www.google.com/drive/',
                'tags': ['google'],
            },
            {
                'integration-name': 'Google Search Ads 360',
                'external-doc-url': 'https://marketingplatform.google.com/about/search-ads-360/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/marketing_platform/search_ads.rst'
                ],
                'tags': ['gmp'],
            },
            {
                'integration-name': 'Google',
                'external-doc-url': 'https://developer.google.com/',
                'tags': ['google'],
            },
            {
                'integration-name': 'Google Spreadsheet',
                'external-doc-url': 'https://www.google.com/intl/en/sheets/about/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/suite/sheets.rst'],
                'tags': ['google'],
            },
            {
                'integration-name': 'Google Cloud Storage Transfer Service',
                'external-doc-url': 'https://cloud.google.com/storage/transfer/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/cloud_storage_transfer_service.rst'
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Kubernetes Engine',
                'external-doc-url': 'https://cloud.google.com/kubernetes_engine/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/kubernetes_engine.rst'
                ],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Machine Learning Engine',
                'external-doc-url': 'https://cloud.google.com/ai-platform/',
                'how-to-guide': ['/docs/apache-airflow-providers-google/operators/cloud/mlengine.rst'],
                'tags': ['gcp'],
            },
            {
                'integration-name': 'Google Cloud Natural Language',
                'external-doc-url': 'https://cloud.google.com/natural-language/',
                'how-to-guide': [
                    '/docs/apache-airflow-providers-google/operators/cloud/natural_language.rst'
                ],
                'tags': ['gcp'],
            },
        ],
        'operators': [
            {
                'integration-name': 'Google Ads',
                'python-modules': ['airflow.providers.google.ads.operators.ads'],
            },
            {
                'integration-name': 'Google AutoML',
                'python-modules': ['airflow.providers.google.cloud.operators.automl'],
            },
            {
                'integration-name': 'Google BigQuery',
                'python-modules': ['airflow.providers.google.cloud.operators.bigquery'],
            },
            {
                'integration-name': 'Google BigQuery Data Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.operators.bigquery_dts'],
            },
            {
                'integration-name': 'Google Bigtable',
                'python-modules': ['airflow.providers.google.cloud.operators.bigtable'],
            },
            {
                'integration-name': 'Google Cloud Build',
                'python-modules': ['airflow.providers.google.cloud.operators.cloud_build'],
            },
            {
                'integration-name': 'Google Cloud Memorystore',
                'python-modules': ['airflow.providers.google.cloud.operators.cloud_memorystore'],
            },
            {
                'integration-name': 'Google Cloud SQL',
                'python-modules': ['airflow.providers.google.cloud.operators.cloud_sql'],
            },
            {
                'integration-name': 'Google Cloud Storage Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.operators.cloud_storage_transfer_service'],
            },
            {
                'integration-name': 'Google Compute Engine',
                'python-modules': ['airflow.providers.google.cloud.operators.compute'],
            },
            {
                'integration-name': 'Google Data Catalog',
                'python-modules': ['airflow.providers.google.cloud.operators.datacatalog'],
            },
            {
                'integration-name': 'Google Dataflow',
                'python-modules': ['airflow.providers.google.cloud.operators.dataflow'],
            },
            {
                'integration-name': 'Google Data Fusion',
                'python-modules': ['airflow.providers.google.cloud.operators.datafusion'],
            },
            {
                'integration-name': 'Google Dataprep',
                'python-modules': ['airflow.providers.google.cloud.operators.dataprep'],
            },
            {
                'integration-name': 'Google Dataproc',
                'python-modules': ['airflow.providers.google.cloud.operators.dataproc'],
            },
            {
                'integration-name': 'Google Datastore',
                'python-modules': ['airflow.providers.google.cloud.operators.datastore'],
            },
            {
                'integration-name': 'Google Cloud Data Loss Prevention (DLP)',
                'python-modules': ['airflow.providers.google.cloud.operators.dlp'],
            },
            {
                'integration-name': 'Google Cloud Functions',
                'python-modules': ['airflow.providers.google.cloud.operators.functions'],
            },
            {
                'integration-name': 'Google Cloud Storage (GCS)',
                'python-modules': ['airflow.providers.google.cloud.operators.gcs'],
            },
            {
                'integration-name': 'Google Kubernetes Engine',
                'python-modules': ['airflow.providers.google.cloud.operators.kubernetes_engine'],
            },
            {
                'integration-name': 'Google Cloud Life Sciences',
                'python-modules': ['airflow.providers.google.cloud.operators.life_sciences'],
            },
            {
                'integration-name': 'Google Machine Learning Engine',
                'python-modules': ['airflow.providers.google.cloud.operators.mlengine'],
            },
            {
                'integration-name': 'Google Cloud Natural Language',
                'python-modules': ['airflow.providers.google.cloud.operators.natural_language'],
            },
            {
                'integration-name': 'Google Cloud Pub/Sub',
                'python-modules': ['airflow.providers.google.cloud.operators.pubsub'],
            },
            {
                'integration-name': 'Google Cloud Spanner',
                'python-modules': ['airflow.providers.google.cloud.operators.spanner'],
            },
            {
                'integration-name': 'Google Cloud Speech-to-Text',
                'python-modules': ['airflow.providers.google.cloud.operators.speech_to_text'],
            },
            {
                'integration-name': 'Google Cloud Stackdriver',
                'python-modules': ['airflow.providers.google.cloud.operators.stackdriver'],
            },
            {
                'integration-name': 'Google Cloud Tasks',
                'python-modules': ['airflow.providers.google.cloud.operators.tasks'],
            },
            {
                'integration-name': 'Google Cloud Text-to-Speech',
                'python-modules': [
                    'airflow.providers.google.cloud.operators.text_to_speech',
                    'airflow.providers.google.cloud.operators.translate_speech',
                ],
            },
            {
                'integration-name': 'Google Cloud Translation',
                'python-modules': [
                    'airflow.providers.google.cloud.operators.translate',
                    'airflow.providers.google.cloud.operators.translate_speech',
                ],
            },
            {
                'integration-name': 'Google Cloud Video Intelligence',
                'python-modules': ['airflow.providers.google.cloud.operators.video_intelligence'],
            },
            {
                'integration-name': 'Google Cloud Vision',
                'python-modules': ['airflow.providers.google.cloud.operators.vision'],
            },
            {
                'integration-name': 'Google Cloud Firestore',
                'python-modules': ['airflow.providers.google.firebase.operators.firestore'],
            },
            {
                'integration-name': 'Google Analytics360',
                'python-modules': ['airflow.providers.google.marketing_platform.operators.analytics'],
            },
            {
                'integration-name': 'Google Campaign Manager',
                'python-modules': ['airflow.providers.google.marketing_platform.operators.campaign_manager'],
            },
            {
                'integration-name': 'Google Display&Video 360',
                'python-modules': ['airflow.providers.google.marketing_platform.operators.display_video'],
            },
            {
                'integration-name': 'Google Search Ads 360',
                'python-modules': ['airflow.providers.google.marketing_platform.operators.search_ads'],
            },
            {
                'integration-name': 'Google Spreadsheet',
                'python-modules': ['airflow.providers.google.suite.operators.sheets'],
            },
        ],
        'sensors': [
            {
                'integration-name': 'Google BigQuery',
                'python-modules': ['airflow.providers.google.cloud.sensors.bigquery'],
            },
            {
                'integration-name': 'Google BigQuery Data Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.sensors.bigquery_dts'],
            },
            {
                'integration-name': 'Google Bigtable',
                'python-modules': ['airflow.providers.google.cloud.sensors.bigtable'],
            },
            {
                'integration-name': 'Google Cloud Storage Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.sensors.cloud_storage_transfer_service'],
            },
            {
                'integration-name': 'Google Dataflow',
                'python-modules': ['airflow.providers.google.cloud.sensors.dataflow'],
            },
            {
                'integration-name': 'Google Dataproc',
                'python-modules': ['airflow.providers.google.cloud.sensors.dataproc'],
            },
            {
                'integration-name': 'Google Cloud Storage (GCS)',
                'python-modules': ['airflow.providers.google.cloud.sensors.gcs'],
            },
            {
                'integration-name': 'Google Cloud Pub/Sub',
                'python-modules': ['airflow.providers.google.cloud.sensors.pubsub'],
            },
            {
                'integration-name': 'Google Campaign Manager',
                'python-modules': ['airflow.providers.google.marketing_platform.sensors.campaign_manager'],
            },
            {
                'integration-name': 'Google Display&Video 360',
                'python-modules': ['airflow.providers.google.marketing_platform.sensors.display_video'],
            },
            {
                'integration-name': 'Google Search Ads 360',
                'python-modules': ['airflow.providers.google.marketing_platform.sensors.search_ads'],
            },
        ],
        'hooks': [
            {'integration-name': 'Google Ads', 'python-modules': ['airflow.providers.google.ads.hooks.ads']},
            {
                'integration-name': 'Google AutoML',
                'python-modules': ['airflow.providers.google.cloud.hooks.automl'],
            },
            {
                'integration-name': 'Google BigQuery',
                'python-modules': ['airflow.providers.google.cloud.hooks.bigquery'],
            },
            {
                'integration-name': 'Google BigQuery Data Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.hooks.bigquery_dts'],
            },
            {
                'integration-name': 'Google Bigtable',
                'python-modules': ['airflow.providers.google.cloud.hooks.bigtable'],
            },
            {
                'integration-name': 'Google Cloud Build',
                'python-modules': ['airflow.providers.google.cloud.hooks.cloud_build'],
            },
            {
                'integration-name': 'Google Cloud Memorystore',
                'python-modules': ['airflow.providers.google.cloud.hooks.cloud_memorystore'],
            },
            {
                'integration-name': 'Google Cloud SQL',
                'python-modules': ['airflow.providers.google.cloud.hooks.cloud_sql'],
            },
            {
                'integration-name': 'Google Cloud Storage Transfer Service',
                'python-modules': ['airflow.providers.google.cloud.hooks.cloud_storage_transfer_service'],
            },
            {
                'integration-name': 'Google Compute Engine',
                'python-modules': [
                    'airflow.providers.google.cloud.hooks.compute',
                    'airflow.providers.google.cloud.hooks.compute_ssh',
                ],
            },
            {
                'integration-name': 'Google Data Catalog',
                'python-modules': ['airflow.providers.google.cloud.hooks.datacatalog'],
            },
            {
                'integration-name': 'Google Dataflow',
                'python-modules': ['airflow.providers.google.cloud.hooks.dataflow'],
            },
            {
                'integration-name': 'Google Data Fusion',
                'python-modules': ['airflow.providers.google.cloud.hooks.datafusion'],
            },
            {
                'integration-name': 'Google Dataprep',
                'python-modules': ['airflow.providers.google.cloud.hooks.dataprep'],
            },
            {
                'integration-name': 'Google Dataproc',
                'python-modules': ['airflow.providers.google.cloud.hooks.dataproc'],
            },
            {
                'integration-name': 'Google Datastore',
                'python-modules': ['airflow.providers.google.cloud.hooks.datastore'],
            },
            {
                'integration-name': 'Google Cloud Data Loss Prevention (DLP)',
                'python-modules': ['airflow.providers.google.cloud.hooks.dlp'],
            },
            {
                'integration-name': 'Google Cloud Functions',
                'python-modules': ['airflow.providers.google.cloud.hooks.functions'],
            },
            {
                'integration-name': 'Google Cloud Storage (GCS)',
                'python-modules': ['airflow.providers.google.cloud.hooks.gcs'],
            },
            {
                'integration-name': 'Google Deployment Manager',
                'python-modules': ['airflow.providers.google.cloud.hooks.gdm'],
            },
            {
                'integration-name': 'Google Cloud Key Management Service (KMS)',
                'python-modules': ['airflow.providers.google.cloud.hooks.kms'],
            },
            {
                'integration-name': 'Google Kubernetes Engine',
                'python-modules': ['airflow.providers.google.cloud.hooks.kubernetes_engine'],
            },
            {
                'integration-name': 'Google Cloud Life Sciences',
                'python-modules': ['airflow.providers.google.cloud.hooks.life_sciences'],
            },
            {
                'integration-name': 'Google Machine Learning Engine',
                'python-modules': ['airflow.providers.google.cloud.hooks.mlengine'],
            },
            {
                'integration-name': 'Google Cloud Natural Language',
                'python-modules': ['airflow.providers.google.cloud.hooks.natural_language'],
            },
            {
                'integration-name': 'Google Cloud OS Login',
                'python-modules': ['airflow.providers.google.cloud.hooks.os_login'],
            },
            {
                'integration-name': 'Google Cloud Pub/Sub',
                'python-modules': ['airflow.providers.google.cloud.hooks.pubsub'],
            },
            {
                'integration-name': 'Google Cloud Secret Manager',
                'python-modules': ['airflow.providers.google.cloud.hooks.secret_manager'],
            },
            {
                'integration-name': 'Google Cloud Spanner',
                'python-modules': ['airflow.providers.google.cloud.hooks.spanner'],
            },
            {
                'integration-name': 'Google Cloud Speech-to-Text',
                'python-modules': ['airflow.providers.google.cloud.hooks.speech_to_text'],
            },
            {
                'integration-name': 'Google Cloud Stackdriver',
                'python-modules': ['airflow.providers.google.cloud.hooks.stackdriver'],
            },
            {
                'integration-name': 'Google Cloud Tasks',
                'python-modules': ['airflow.providers.google.cloud.hooks.tasks'],
            },
            {
                'integration-name': 'Google Cloud Text-to-Speech',
                'python-modules': ['airflow.providers.google.cloud.hooks.text_to_speech'],
            },
            {
                'integration-name': 'Google Cloud Translation',
                'python-modules': ['airflow.providers.google.cloud.hooks.translate'],
            },
            {
                'integration-name': 'Google Cloud Video Intelligence',
                'python-modules': ['airflow.providers.google.cloud.hooks.video_intelligence'],
            },
            {
                'integration-name': 'Google Cloud Vision',
                'python-modules': ['airflow.providers.google.cloud.hooks.vision'],
            },
            {
                'integration-name': 'Google',
                'python-modules': ['airflow.providers.google.common.hooks.base_google'],
            },
            {
                'integration-name': 'Google Discovery API',
                'python-modules': ['airflow.providers.google.common.hooks.discovery_api'],
            },
            {
                'integration-name': 'Google Cloud Firestore',
                'python-modules': ['airflow.providers.google.firebase.hooks.firestore'],
            },
            {
                'integration-name': 'Google Analytics360',
                'python-modules': ['airflow.providers.google.marketing_platform.hooks.analytics'],
            },
            {
                'integration-name': 'Google Campaign Manager',
                'python-modules': ['airflow.providers.google.marketing_platform.hooks.campaign_manager'],
            },
            {
                'integration-name': 'Google Display&Video 360',
                'python-modules': ['airflow.providers.google.marketing_platform.hooks.display_video'],
            },
            {
                'integration-name': 'Google Search Ads 360',
                'python-modules': ['airflow.providers.google.marketing_platform.hooks.search_ads'],
            },
            {
                'integration-name': 'Google Drive',
                'python-modules': ['airflow.providers.google.suite.hooks.drive'],
            },
            {
                'integration-name': 'Google Spreadsheet',
                'python-modules': ['airflow.providers.google.suite.hooks.sheets'],
            },
        ],
        'transfers': [
            {
                'source-integration-name': 'Presto',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/presto_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.presto_to_gcs',
            },
            {
                'source-integration-name': 'SQL',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.sql_to_gcs',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Google Drive',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/gcs_to_gdrive.rst',
                'python-module': 'airflow.providers.google.suite.transfers.gcs_to_gdrive',
            },
            {
                'source-integration-name': 'Microsoft SQL Server (MSSQL)',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.mssql_to_gcs',
            },
            {
                'source-integration-name': 'Microsoft Azure FileShare',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/azure_fileshare_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.azure_fileshare_to_gcs',
            },
            {
                'source-integration-name': 'Apache Cassandra',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.cassandra_to_gcs',
            },
            {
                'source-integration-name': 'Google Spreadsheet',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/sheets_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.sheets_to_gcs',
            },
            {
                'source-integration-name': 'Amazon Simple Storage Service (S3)',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/s3_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.s3_to_gcs',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'SSH File Transfer Protocol (SFTP)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/gcs_to_sftp.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.gcs_to_sftp',
            },
            {
                'source-integration-name': 'PostgreSQL',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.postgres_to_gcs',
            },
            {
                'source-integration-name': 'Google BigQuery',
                'target-integration-name': 'MySQL',
                'python-module': 'airflow.providers.google.cloud.transfers.bigquery_to_mysql',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Google BigQuery',
                'python-module': 'airflow.providers.google.cloud.transfers.gcs_to_bigquery',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/gcs_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.gcs_to_gcs',
            },
            {
                'source-integration-name': 'Facebook Ads',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/facebook_ads_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.facebook_ads_to_gcs',
            },
            {
                'source-integration-name': 'SSH File Transfer Protocol (SFTP)',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/sftp_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.sftp_to_gcs',
            },
            {
                'source-integration-name': 'Microsoft Azure Data Lake Storage',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.adls_to_gcs',
            },
            {
                'source-integration-name': 'Google BigQuery',
                'target-integration-name': 'Google BigQuery',
                'python-module': 'airflow.providers.google.cloud.transfers.bigquery_to_bigquery',
            },
            {
                'source-integration-name': 'MySQL',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.mysql_to_gcs',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/mysql_to_gcs.rst',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Google Spreadsheet',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/gcs_to_sheets.rst',
                'python-module': 'airflow.providers.google.suite.transfers.gcs_to_sheets',
            },
            {
                'source-integration-name': 'Local',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/local_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.local_to_gcs',
            },
            {
                'source-integration-name': 'Google BigQuery',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.cloud.transfers.bigquery_to_gcs',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Local',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/gcs_to_local.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.gcs_to_local',
            },
            {
                'source-integration-name': 'Salesforce',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-google/operators/transfer/salesforce_to_gcs.rst',
                'python-module': 'airflow.providers.google.cloud.transfers.salesforce_to_gcs',
            },
            {
                'source-integration-name': 'Google Ads',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'python-module': 'airflow.providers.google.ads.transfers.ads_to_gcs',
            },
        ],
        'hook-class-names': [
            'airflow.providers.google.cloud.hooks.dataprep.GoogleDataprepHook',
            'airflow.providers.google.cloud.hooks.cloud_sql.CloudSQLHook',
            'airflow.providers.google.cloud.hooks.cloud_sql.CloudSQLDatabaseHook',
            'airflow.providers.google.cloud.hooks.compute_ssh.ComputeEngineSSHHook',
            'airflow.providers.google.cloud.hooks.bigquery.BigQueryHook',
            'airflow.providers.google.common.hooks.base_google.GoogleBaseHook',
        ],
        'extra-links': [
            'airflow.providers.google.cloud.operators.bigquery.BigQueryConsoleLink',
            'airflow.providers.google.cloud.operators.bigquery.BigQueryConsoleIndexableLink',
            'airflow.providers.google.cloud.operators.mlengine.AIPlatformConsoleLink',
        ],
    }
