#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CONTEXT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CONTEXT_DIR/../.. >/dev/null 2>&1 && pwd )"

set -e
set -x

${SCRIPT_DIR}/deploy.sh

source $CONTEXT_DIR/.env
CURRENT_DEV_IMAGE_FULL=${DEV_IMAGE_FULL}
cd $ROOT_DIR
source $ROOT_DIR/.env

DEV_IMAGE_FULL=${CURRENT_DEV_IMAGE_FULL} \
CONTEXT_DIR=${CONTEXT_DIR} \
    docker compose \
    -f docker-compose-dev.yaml \
    -f ${CONTEXT_DIR}/docker-compose-dev.yml \
    up -d