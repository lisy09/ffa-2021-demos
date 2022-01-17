#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CONTEXT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CONTEXT_DIR/../.. >/dev/null 2>&1 && pwd )"

set -e
set -x

source $CONTEXT_DIR/.env
CURRENT_DEV_IMAGE_FULL=${DEV_IMAGE_FULL}
cd $ROOT_DIR
source $ROOT_DIR/.env
DEV_IMAGE_FULL=${DEV_IMAGE_FULL}

docker compose \
    -f docker-compose-dev.yaml down

cd ${SCRIPT_DIR}
${SCRIPT_DIR}/undeploy.sh