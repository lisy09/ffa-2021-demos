#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

readonly MERGE_TARGET_DIR=$ROOT_DIR/$MERGE_DIR

cp $CUSTOM_DIR/base-requirements.txt $MERGE_TARGET_DIR/base-requirements.txt
cp $CUSTOM_DIR/requirements.txt $MERGE_TARGET_DIR/requirements.txt
cp $CUSTOM_DIR/setup.py $MERGE_TARGET_DIR/setup.py

cp $CUSTOM_DIR/lib/airflow/setup.py $MERGE_TARGET_DIR/lib/airflow/setup.py
cp $CUSTOM_DIR/lib/airflow/setup.cfg $MERGE_TARGET_DIR/lib/airflow/setup.cfg
cp $CUSTOM_DIR/lib/notification_service/setup.py $MERGE_TARGET_DIR/lib/notification_service/setup.py