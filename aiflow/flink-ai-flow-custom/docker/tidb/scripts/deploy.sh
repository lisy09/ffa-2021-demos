#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"

set -e
set -x

if [ "$(docker network ls -f name=app -q)" = "" ]; then 
    docker network create app; 
fi
cd ${ROOT_DIR}
docker compose \
    --env-file=.env \
    -f docker-compose.yml up -d