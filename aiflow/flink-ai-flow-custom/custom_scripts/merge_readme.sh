#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

readonly MERGE_TARGET_DIR=$ROOT_DIR/$MERGE_DIR

mv $MERGE_TARGET_DIR/README.md $MERGE_TARGET_DIR/README_upstream.md
cp $CUSTOM_DIR/README.md $MERGE_TARGET_DIR/README.md