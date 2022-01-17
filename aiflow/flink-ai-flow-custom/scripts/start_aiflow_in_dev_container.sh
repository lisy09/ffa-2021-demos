#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env

COMMANDS=mysql,awk
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -e
set -x

mysql_cmd="mysql -h ${MYSQL_HOSTNAME} -P ${MYSQL_PORT} -u ${MYSQL_USER} -p${MYSQL_PASSWORD}"

set +e
$mysql_cmd -e "drop database aiflow; drop database airflow; drop database notification_service;"
set -e

$mysql_cmd -e "set global explicit_defaults_for_timestamp=1;"
$mysql_cmd -e "CREATE DATABASE aiflow CHARACTER SET UTF8mb3 COLLATE utf8_general_ci;"
$mysql_cmd -e "CREATE DATABASE airflow CHARACTER SET UTF8mb3 COLLATE utf8_general_ci;"
$mysql_cmd -e "CREATE DATABASE notification_service CHARACTER SET UTF8mb3 COLLATE utf8_general_ci;"

export AIFLOW_HOME=${HOME}/aiflow
export AIRFLOW_HOME=${HOME}/airflow
rm -rf ${AIFLOW_HOME} ${AIRFLOW_HOME}

MYSQL_CONN=mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOSTNAME}:${MYSQL_PORT}
start-all-aiflow-services.sh ${MYSQL_CONN}/notification_service ${MYSQL_CONN}/airflow ${MYSQL_CONN}/aiflow
