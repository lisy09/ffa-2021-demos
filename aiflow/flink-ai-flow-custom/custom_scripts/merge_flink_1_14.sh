#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

readonly MERGE_TARGET_DIR=$ROOT_DIR/$MERGE_DIR


readonly FLINK_PLUGIN_DIR=ai_flow_plugins/job_plugins/flink
cp $CUSTOM_DIR/$FLINK_PLUGIN_DIR/__init__.py $MERGE_TARGET_DIR/$FLINK_PLUGIN_DIR/__init__.py
cp $CUSTOM_DIR/$FLINK_PLUGIN_DIR/flink_env.py $MERGE_TARGET_DIR/$FLINK_PLUGIN_DIR/flink_env.py
cp $CUSTOM_DIR/$FLINK_PLUGIN_DIR/flink_wrapped_env.py $MERGE_TARGET_DIR/$FLINK_PLUGIN_DIR/flink_wrapped_env.py
cp $CUSTOM_DIR/$FLINK_PLUGIN_DIR/flink_processor.py $MERGE_TARGET_DIR/$FLINK_PLUGIN_DIR/flink_processor.py

JOB_PLUGIN_TEST_DIR=ai_flow_plugins/tests/job_plugins
cp $CUSTOM_DIR/$JOB_PLUGIN_TEST_DIR/ut_workflows/workflows/test_flink/test_flink_processor.py $MERGE_TARGET_DIR/$JOB_PLUGIN_TEST_DIR/ut_workflows/workflows/test_flink/test_flink_processor.py