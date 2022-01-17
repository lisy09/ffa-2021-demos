#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env

COMMANDS=docker,awk
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -e
set -x

IFS=',' read -a images <<< ${DELETE_IMAGE_LIST}
for image in ${images[@]}; do
    docker rmi -f \
        $(docker images --format "{{.Repository}}:{{.Tag}} {{.ID}}" | grep -e "^${image}" | awk '{print $2}')
done