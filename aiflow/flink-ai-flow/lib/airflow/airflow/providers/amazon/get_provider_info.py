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
        'package-name': 'apache-airflow-providers-amazon',
        'name': 'Amazon',
        'description': 'Amazon integration (including `Amazon Web Services (AWS) <https://aws.amazon.com/>`__).\n',
        'versions': ['1.0.0'],
        'integrations': [
            {
                'integration-name': 'Amazon Athena',
                'external-doc-url': 'https://aws.amazon.com/athena/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon CloudFormation',
                'external-doc-url': 'https://aws.amazon.com/cloudformation/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon CloudWatch Logs',
                'external-doc-url': 'https://aws.amazon.com/cloudwatch/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon DataSync',
                'external-doc-url': 'https://aws.amazon.com/datasync/',
                'how-to-guide': ['/docs/apache-airflow-providers-amazon/operators/datasync.rst'],
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon DynamoDB',
                'external-doc-url': 'https://aws.amazon.com/dynamodb/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon EC2',
                'external-doc-url': 'https://aws.amazon.com/ec2/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon ECS',
                'external-doc-url': 'https://aws.amazon.com/ecs/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon ElastiCache',
                'external-doc-url': 'https://aws.amazon.com/elasticache/redis//',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon EMR',
                'external-doc-url': 'https://aws.amazon.com/emr/',
                'how-to-guide': ['/docs/apache-airflow-providers-amazon/operators/emr.rst'],
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Glacier',
                'external-doc-url': 'https://aws.amazon.com/glacier/',
                'how-to-guide': ['/docs/apache-airflow-providers-amazon/operators/glacier.rst'],
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Kinesis Data Firehose',
                'external-doc-url': 'https://aws.amazon.com/kinesis/data-firehose/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Redshift',
                'external-doc-url': 'https://aws.amazon.com/redshift/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon SageMaker',
                'external-doc-url': 'https://aws.amazon.com/sagemaker/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon SecretsManager',
                'external-doc-url': 'https://aws.amazon.com/secrets-manager/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Simple Email Service (SES)',
                'external-doc-url': 'https://aws.amazon.com/ses/',
                'how-to-guide': ['/docs/apache-airflow-providers-amazon/operators/ecs.rst'],
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Simple Notification Service (SNS)',
                'external-doc-url': 'https://aws.amazon.com/sns/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Simple Queue Service (SQS)',
                'external-doc-url': 'https://aws.amazon.com/sqs/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Simple Storage Service (S3)',
                'external-doc-url': 'https://aws.amazon.com/s3/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'Amazon Web Services',
                'external-doc-url': 'https://aws.amazon.com/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'AWS Batch',
                'external-doc-url': 'https://aws.amazon.com/batch/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'AWS DataSync',
                'external-doc-url': 'https://aws.amazon.com/datasync/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'AWS Glue',
                'external-doc-url': 'https://aws.amazon.com/glue/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'AWS Lambda',
                'external-doc-url': 'https://aws.amazon.com/lambda/',
                'tags': ['aws'],
            },
            {
                'integration-name': 'AWS Step Functions',
                'external-doc-url': 'https://aws.amazon.com/step-functions/',
                'tags': ['aws'],
            },
        ],
        'operators': [
            {
                'integration-name': 'Amazon Athena',
                'python-modules': ['airflow.providers.amazon.aws.operators.athena'],
            },
            {
                'integration-name': 'AWS Batch',
                'python-modules': ['airflow.providers.amazon.aws.operators.batch'],
            },
            {
                'integration-name': 'Amazon CloudFormation',
                'python-modules': ['airflow.providers.amazon.aws.operators.cloud_formation'],
            },
            {
                'integration-name': 'Amazon DataSync',
                'python-modules': ['airflow.providers.amazon.aws.operators.datasync'],
            },
            {
                'integration-name': 'Amazon EC2',
                'python-modules': [
                    'airflow.providers.amazon.aws.operators.ec2_start_instance',
                    'airflow.providers.amazon.aws.operators.ec2_stop_instance',
                ],
            },
            {
                'integration-name': 'Amazon ECS',
                'python-modules': ['airflow.providers.amazon.aws.operators.ecs'],
            },
            {
                'integration-name': 'Amazon EMR',
                'python-modules': [
                    'airflow.providers.amazon.aws.operators.emr_add_steps',
                    'airflow.providers.amazon.aws.operators.emr_create_job_flow',
                    'airflow.providers.amazon.aws.operators.emr_modify_cluster',
                    'airflow.providers.amazon.aws.operators.emr_terminate_job_flow',
                ],
            },
            {
                'integration-name': 'Amazon Glacier',
                'python-modules': ['airflow.providers.amazon.aws.operators.glacier'],
            },
            {
                'integration-name': 'AWS Glue',
                'python-modules': ['airflow.providers.amazon.aws.operators.glue'],
            },
            {
                'integration-name': 'Amazon Simple Storage Service (S3)',
                'python-modules': [
                    'airflow.providers.amazon.aws.operators.s3_bucket',
                    'airflow.providers.amazon.aws.operators.s3_copy_object',
                    'airflow.providers.amazon.aws.operators.s3_delete_objects',
                    'airflow.providers.amazon.aws.operators.s3_file_transform',
                    'airflow.providers.amazon.aws.operators.s3_list',
                ],
            },
            {
                'integration-name': 'Amazon SageMaker',
                'python-modules': [
                    'airflow.providers.amazon.aws.operators.sagemaker_base',
                    'airflow.providers.amazon.aws.operators.sagemaker_endpoint',
                    'airflow.providers.amazon.aws.operators.sagemaker_endpoint_config',
                    'airflow.providers.amazon.aws.operators.sagemaker_model',
                    'airflow.providers.amazon.aws.operators.sagemaker_processing',
                    'airflow.providers.amazon.aws.operators.sagemaker_training',
                    'airflow.providers.amazon.aws.operators.sagemaker_transform',
                    'airflow.providers.amazon.aws.operators.sagemaker_tuning',
                ],
            },
            {
                'integration-name': 'Amazon Simple Notification Service (SNS)',
                'python-modules': ['airflow.providers.amazon.aws.operators.sns'],
            },
            {
                'integration-name': 'Amazon Simple Queue Service (SQS)',
                'python-modules': ['airflow.providers.amazon.aws.operators.sqs'],
            },
            {
                'integration-name': 'AWS Step Functions',
                'python-modules': [
                    'airflow.providers.amazon.aws.operators.step_function_get_execution_output',
                    'airflow.providers.amazon.aws.operators.step_function_start_execution',
                ],
            },
        ],
        'sensors': [
            {
                'integration-name': 'Amazon Athena',
                'python-modules': ['airflow.providers.amazon.aws.sensors.athena'],
            },
            {
                'integration-name': 'Amazon CloudFormation',
                'python-modules': ['airflow.providers.amazon.aws.sensors.cloud_formation'],
            },
            {
                'integration-name': 'Amazon EC2',
                'python-modules': ['airflow.providers.amazon.aws.sensors.ec2_instance_state'],
            },
            {
                'integration-name': 'Amazon EMR',
                'python-modules': [
                    'airflow.providers.amazon.aws.sensors.emr_base',
                    'airflow.providers.amazon.aws.sensors.emr_job_flow',
                    'airflow.providers.amazon.aws.sensors.emr_step',
                ],
            },
            {
                'integration-name': 'Amazon Glacier',
                'python-modules': ['airflow.providers.amazon.aws.sensors.glacier'],
            },
            {
                'integration-name': 'AWS Glue',
                'python-modules': [
                    'airflow.providers.amazon.aws.sensors.glue',
                    'airflow.providers.amazon.aws.sensors.glue_catalog_partition',
                ],
            },
            {
                'integration-name': 'Amazon Redshift',
                'python-modules': ['airflow.providers.amazon.aws.sensors.redshift'],
            },
            {
                'integration-name': 'Amazon Simple Storage Service (S3)',
                'python-modules': [
                    'airflow.providers.amazon.aws.sensors.s3_key',
                    'airflow.providers.amazon.aws.sensors.s3_keys_unchanged',
                    'airflow.providers.amazon.aws.sensors.s3_prefix',
                ],
            },
            {
                'integration-name': 'Amazon SageMaker',
                'python-modules': [
                    'airflow.providers.amazon.aws.sensors.sagemaker_base',
                    'airflow.providers.amazon.aws.sensors.sagemaker_endpoint',
                    'airflow.providers.amazon.aws.sensors.sagemaker_training',
                    'airflow.providers.amazon.aws.sensors.sagemaker_transform',
                    'airflow.providers.amazon.aws.sensors.sagemaker_tuning',
                ],
            },
            {
                'integration-name': 'Amazon Simple Queue Service (SQS)',
                'python-modules': ['airflow.providers.amazon.aws.sensors.sqs'],
            },
            {
                'integration-name': 'AWS Step Functions',
                'python-modules': ['airflow.providers.amazon.aws.sensors.step_function_execution'],
            },
        ],
        'hooks': [
            {
                'integration-name': 'Amazon Athena',
                'python-modules': ['airflow.providers.amazon.aws.hooks.athena'],
            },
            {
                'integration-name': 'Amazon DynamoDB',
                'python-modules': [
                    'airflow.providers.amazon.aws.hooks.dynamodb',
                    'airflow.providers.amazon.aws.hooks.aws_dynamodb',
                ],
            },
            {
                'integration-name': 'Amazon Web Services',
                'python-modules': ['airflow.providers.amazon.aws.hooks.base_aws'],
            },
            {
                'integration-name': 'AWS Batch',
                'python-modules': [
                    'airflow.providers.amazon.aws.hooks.batch_client',
                    'airflow.providers.amazon.aws.hooks.batch_waiters',
                ],
            },
            {
                'integration-name': 'Amazon CloudFormation',
                'python-modules': ['airflow.providers.amazon.aws.hooks.cloud_formation'],
            },
            {
                'integration-name': 'Amazon DataSync',
                'python-modules': ['airflow.providers.amazon.aws.hooks.datasync'],
            },
            {'integration-name': 'Amazon EC2', 'python-modules': ['airflow.providers.amazon.aws.hooks.ec2']},
            {
                'integration-name': 'Amazon ElastiCache',
                'python-modules': ['airflow.providers.amazon.aws.hooks.elasticache_replication_group'],
            },
            {'integration-name': 'Amazon EMR', 'python-modules': ['airflow.providers.amazon.aws.hooks.emr']},
            {
                'integration-name': 'Amazon Glacier',
                'python-modules': ['airflow.providers.amazon.aws.hooks.glacier'],
            },
            {
                'integration-name': 'AWS Glue',
                'python-modules': [
                    'airflow.providers.amazon.aws.hooks.glue',
                    'airflow.providers.amazon.aws.hooks.glue_catalog',
                ],
            },
            {
                'integration-name': 'Amazon Kinesis Data Firehose',
                'python-modules': ['airflow.providers.amazon.aws.hooks.kinesis'],
            },
            {
                'integration-name': 'AWS Lambda',
                'python-modules': ['airflow.providers.amazon.aws.hooks.lambda_function'],
            },
            {
                'integration-name': 'Amazon CloudWatch Logs',
                'python-modules': ['airflow.providers.amazon.aws.hooks.logs'],
            },
            {
                'integration-name': 'Amazon Redshift',
                'python-modules': ['airflow.providers.amazon.aws.hooks.redshift'],
            },
            {
                'integration-name': 'Amazon Simple Storage Service (S3)',
                'python-modules': ['airflow.providers.amazon.aws.hooks.s3'],
            },
            {
                'integration-name': 'Amazon SageMaker',
                'python-modules': ['airflow.providers.amazon.aws.hooks.sagemaker'],
            },
            {
                'integration-name': 'Amazon Simple Email Service (SES)',
                'python-modules': ['airflow.providers.amazon.aws.hooks.ses'],
            },
            {
                'integration-name': 'Amazon SecretsManager',
                'python-modules': ['airflow.providers.amazon.aws.hooks.secrets_manager'],
            },
            {
                'integration-name': 'Amazon Simple Notification Service (SNS)',
                'python-modules': ['airflow.providers.amazon.aws.hooks.sns'],
            },
            {
                'integration-name': 'Amazon Simple Queue Service (SQS)',
                'python-modules': ['airflow.providers.amazon.aws.hooks.sqs'],
            },
            {
                'integration-name': 'AWS Step Functions',
                'python-modules': ['airflow.providers.amazon.aws.hooks.step_function'],
            },
        ],
        'transfers': [
            {
                'source-integration-name': 'Amazon DynamoDB',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.dynamodb_to_s3',
            },
            {
                'source-integration-name': 'Google Cloud Storage (GCS)',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.gcs_to_s3',
            },
            {
                'source-integration-name': 'Amazon Glacier',
                'target-integration-name': 'Google Cloud Storage (GCS)',
                'how-to-guide': '/docs/apache-airflow-providers-amazon/operators/transfer/glacier_to_gcs.rst',
                'python-module': 'airflow.providers.amazon.aws.transfers.glacier_to_gcs',
            },
            {
                'source-integration-name': 'Google',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'how-to-guide': '/docs/apache-airflow-providers-amazon/operators/google_api_to_s3_transfer.rst',
                'python-module': 'airflow.providers.amazon.aws.transfers.google_api_to_s3',
            },
            {
                'source-integration-name': 'Apache Hive',
                'target-integration-name': 'Amazon DynamoDB',
                'python-module': 'airflow.providers.amazon.aws.transfers.hive_to_dynamodb',
            },
            {
                'source-integration-name': 'Internet Message Access Protocol (IMAP)',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'how-to-guide': '/docs/apache-airflow-providers-amazon/operators/imap_attachment_to_s3.rst',
                'python-module': 'airflow.providers.amazon.aws.transfers.imap_attachment_to_s3',
            },
            {
                'source-integration-name': 'MongoDB',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.mongo_to_s3',
            },
            {
                'source-integration-name': 'MySQL',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.mysql_to_s3',
            },
            {
                'source-integration-name': 'Amazon Redshift',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.redshift_to_s3',
            },
            {
                'source-integration-name': 'Amazon Simple Storage Service (S3)',
                'target-integration-name': 'Amazon Redshift',
                'how-to-guide': '/docs/apache-airflow-providers-amazon/operators/s3_to_redshift.rst',
                'python-module': 'airflow.providers.amazon.aws.transfers.s3_to_redshift',
            },
            {
                'source-integration-name': 'Amazon Simple Storage Service (S3)',
                'target-integration-name': 'SSH File Transfer Protocol (SFTP)',
                'python-module': 'airflow.providers.amazon.aws.transfers.s3_to_sftp',
            },
            {
                'source-integration-name': 'SSH File Transfer Protocol (SFTP)',
                'target-integration-name': 'Amazon Simple Storage Service (S3)',
                'python-module': 'airflow.providers.amazon.aws.transfers.sftp_to_s3',
            },
        ],
        'hook-class-names': [
            'airflow.providers.amazon.aws.hooks.s3.S3Hook',
            'airflow.providers.amazon.aws.hooks.base_aws.AwsBaseHook',
            'airflow.providers.amazon.aws.hooks.emr.EmrHook',
        ],
    }
