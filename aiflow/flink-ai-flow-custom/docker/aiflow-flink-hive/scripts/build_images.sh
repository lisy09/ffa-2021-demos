#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly DOCKERFILE_DIR="$( cd $ROOT_DIR/docker >/dev/null 2>&1 && pwd )"

set -e
set -x

${DOCKERFILE_DIR}/hadoop-base/build.sh
${DOCKERFILE_DIR}/hadoop-namenode/build.sh
${DOCKERFILE_DIR}/hadoop-datanode/build.sh
${DOCKERFILE_DIR}/hive/build.sh
${DOCKERFILE_DIR}/flink-hive/build.sh
${DOCKERFILE_DIR}/aiflow-dev/build.sh