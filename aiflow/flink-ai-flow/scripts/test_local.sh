#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env

echo "Install notification java client..."
cd $ROOT_DIR/lib/notification_service/java && mvn install -DskipTests=true

echo "Install ai_flow java client..."
cd $ROOT_DIR/ai_flow/java && mvn install -DskipTests=true

echo "Run tests..."
$ROOT_DIR/run_tests.sh