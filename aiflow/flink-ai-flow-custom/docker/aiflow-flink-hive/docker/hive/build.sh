#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/../.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env

COMMANDS=docker
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -e
set -x

IFS=',' read -a base_build_args <<< ${HIVE_BUILD_ARGS}
for BUILD_ARG in ${base_build_args[@]}; do
    build_args+=" --build-arg ${BUILD_ARG}"
done

docker build ${build_args} \
    -t ${HIVE_IMAGE_FULL} \
    -f $SCRIPT_DIR/$HIVE_DOCKERFILE \
    $SCRIPT_DIR/$HIVE_CONTEXT