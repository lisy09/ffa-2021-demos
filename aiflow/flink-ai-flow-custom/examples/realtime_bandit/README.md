# realtime_bandit

This is a demo project to implement realtime bandit algorithm with flink-ai-flow.

# How to run

Before running the workflow, you need to setup the cluster.

```bash
# move to flink-ai-flow parent dir
cd ${realtime_bandit_dir}/../..
make aiflow-flink-hive-dev-deploy
```

Then you run command in docker container

```bash
docker exec -it flink-ai-flow-dev bash

# in container
cd /workspace
# run ai-flow cluster
make start-local
# run workflow
python examples/realtime_bandit/workflows/realtime_bandit/realtime_bandit.py
```