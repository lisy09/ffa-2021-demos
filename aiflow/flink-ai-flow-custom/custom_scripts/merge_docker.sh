#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

readonly MERGE_TARGET_DIR=$ROOT_DIR/$MERGE_DIR

cp -r $CUSTOM_DIR/docker/ $MERGE_TARGET_DIR/docker/

tee -a $MERGE_TARGET_DIR/.dockerignore > /dev/null <<EOT

# Include docker/ 
!docker
# Include Makefile
!Makefile
# Include scripts/
!scripts
# Include dotenv
!.env
EOT

cp -r $CUSTOM_DIR/docker-compose-dev.yaml $MERGE_TARGET_DIR/docker-compose-dev.yaml
cp -r $CUSTOM_DIR/docker-compose.yaml $MERGE_TARGET_DIR/docker-compose.yaml