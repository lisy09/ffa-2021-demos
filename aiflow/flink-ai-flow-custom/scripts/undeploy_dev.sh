#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"

set -e
set -x

cd $ROOT_DIR
source $ROOT_DIR/.env

docker compose \
    -f docker-compose-dev.yaml \
    down