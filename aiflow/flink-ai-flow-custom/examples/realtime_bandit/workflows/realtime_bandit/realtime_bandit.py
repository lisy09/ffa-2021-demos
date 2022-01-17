from typing import Tuple
from ai_flow_plugins.job_plugins.flink.flink_env import FlinkBatchEnv
import os
import shutil
import time

import ai_flow as af
from ai_flow.util.path_util import get_file_dir
import ai_flow_plugins.job_plugins.flink as flink_plugin

from deps.config.config import load_project_config
import deps.realtime_bandit_processors.hive_user_feature_generator as hive_user_feature_generator
import deps.realtime_bandit_processors.hive_to_tidb as hive_to_tidb

def build_workflow():
    yaml_config = load_project_config()
    af.init_ai_flow_context()
    project_name = af.current_project_config().get_project_name()
    artifact_prefix = project_name + "."
    with af.job_config('gen_static_user_feature_to_hive'):
        flink_plugin.set_flink_env(flink_plugin.FlinkBatchEnv())
        config = yaml_config['gen_static_user_feature_to_hive']
        af.user_define_operation(
            processor=hive_user_feature_generator.HiveUserFeatureGenerator(),
            output_num=0,
            name='gen_static_user_feature_to_hive',
            gen_config=config,
        )
    with af.job_config('copy_static_user_feature_from_hive_to_tidb'):
        flink_plugin.set_flink_env(hive_to_tidb.HiveToTidbTableEnv())
        config = yaml_config['copy_static_user_feature_from_hive_to_tidb']
        af.user_define_operation(
            processor=hive_to_tidb.UserFeatureHiveToTidb(),
            output_num=0,
            name='copy_static_user_feature_from_hive_to_tidb',
            conf=config,
        )


def get_execution_result_dir():
    return os.path.join(get_file_dir(__file__), "temp")


def run_workflow():
    workflow_name = af.current_workflow_config().workflow_name
    stop_workflow_executions(workflow_name)
    af.workflow_operation.submit_workflow(workflow_name)
    af.workflow_operation.start_new_workflow_execution(workflow_name)


def stop_workflow_executions(workflow_name):
    workflow_executions = af.workflow_operation.list_workflow_executions(
        workflow_name)
    for workflow_execution in workflow_executions:
        af.workflow_operation.stop_workflow_execution(
            workflow_execution.workflow_execution_id)


def clear_project_dir():
    execution_result_dir = get_execution_result_dir()
    shutil.rmtree(execution_result_dir, ignore_errors=True)


def watch_running_and_stop_gracefully():
    workflow_name = af.current_workflow_config().workflow_name
    while True:
        try:
            workflow_executions = af.workflow_operation.list_workflow_executions(
                workflow_name)
            all_finished = True
            for workflow_execution in workflow_executions:
                if workflow_execution.status != "FINISHED":
                    all_finished = False
                    break
            if all_finished:
                break
            time.sleep(5)
        except KeyboardInterrupt:
            print("stop workflow manually...")
            stop_workflow_executions(workflow_name)
            break


if __name__ == '__main__':
    clear_project_dir()
    print("building workflow...")
    build_workflow()
    print("submitting workflow...")
    run_workflow()
    print("submitting workflow... finished!")
    print("watching workflow...")
    watch_running_and_stop_gracefully()
    print("workflow stopped. exit.")
