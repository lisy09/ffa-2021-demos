#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env


usage() {
  echo -n "Usage: ${0} " >&2
  echo -n "--coverage|-c run in coverage test mode " >&2
  echo >&2
}

while [[ ${#} -gt 0 ]]; do
  parameter="${1}"

  case "${parameter}" in
    --coverage|-c)
      COVERAGE_MODE=TRUE
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Invalid parameter: ${parameter}" >&2
      exit 1
      ;;
  esac

  shift
done

COMMANDS=pytest,coverage
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -e
set -x

TEST_TARGETS=


AIFLOW_PLUGIN_TEST_DIR=$ROOT_DIR/ai_flow_plugins/tests
AIFLOW_PLUGIN_INTEGRATION_TEST_DIR=$AIFLOW_PLUGIN_TEST_DIR/integration_test/workflows
TEST_TARGETS+=" ${AIFLOW_PLUGIN_INTEGRATION_TEST_DIR}/test_bash"
TEST_TARGETS+=" ${AIFLOW_PLUGIN_INTEGRATION_TEST_DIR}/test_python"
TEST_TARGETS+=" ${AIFLOW_PLUGIN_INTEGRATION_TEST_DIR}/test_flink"
TEST_TARGETS+=" ${AIFLOW_PLUGIN_INTEGRATION_TEST_DIR}/test_action_on_event"
TEST_TARGETS+=" ${AIFLOW_PLUGIN_INTEGRATION_TEST_DIR}/test_periodic_workflow"

AIFLOW_PLUGIN_SCHEDULER_INTEGRATION_TEST_DIR_AIRFLOW=$AIFLOW_PLUGIN_TEST_DIR/integration_scheduler/scheduler_plugins/airflow
TEST_TARGETS+=" ${AIFLOW_PLUGIN_SCHEDULER_INTEGRATION_TEST_DIR_AIRFLOW}"



if [ "$COVERAGE_MODE" != "TRUE" ]; then
    echo "test mode ..."
    pytest ${TEST_TARGETS} -v -x
else
    echo "coverage mode ..."
    coverage run -m pytest ${TEST_TARGETS}
    rm -rf $ROOT_DIR/htmlcov && coverage html
    coverage report -m
fi