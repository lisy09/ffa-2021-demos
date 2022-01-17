# flink-ai-flow

## CHANGE LOGS

Latest related alibaba version
- git commit: 455bef7fd9c08aaa6f97152d9f0bf29ede329ce9
- time: Fri Jan 14 17:59:36 2022 +0800

## IN-PROGRESS

## TODO

- optimize the size of dev/base docker images
- add ai_flow.api.ops.rest_model_serving for model serving as API
- add ai_flow.api.contrib.processors.observable_model_processors.ObservableModelProcessor to be use in ai_flow.api.ops.train/evaluate/model_validate/push_model, to send model metric automatically to metric service
- add k8s deployment manual
- add Grafana monitoring dashboard using metric data from metric service
- add ai_flow_plugins.job_plugin.storage_scheduler for providing database (TiDB/redis/Pulsar/MinIO)
- add Loki+Grafana log tracking for projects

## API docs

Please check `./docs/html/index.html`.

## Upstream README

Please check [Upstream READEME](./README_upstream.md).