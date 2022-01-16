#!/bin/bash

PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR="$( cd $PARENT_DIR/.. >/dev/null 2>&1 && pwd )"
MANIFEST_DIR=$ROOT_DIR/manifest

source $ROOT_DIR/.env
set -e

COMMANDS=kubectl
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -x

kubectl apply -k ${MANIFEST_DIR}/observability-kustomize

# work-around for ingress of dapr-dashboard
kubectl -n dapr-system patch deployment dapr-dashboard -p '{"spec":{"template":{"spec":{"containers":[{"name":"dapr-dashboard","env":[{"name":"SERVER_BASE_HREF", "value":"/dapr-dashboard/"}]}]}}}}'