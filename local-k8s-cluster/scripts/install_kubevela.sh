#!/bin/bash

PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR="$( cd $PARENT_DIR/.. >/dev/null 2>&1 && pwd )"
MANIFEST_DIR=$ROOT_DIR/manifest

source $ROOT_DIR/.env
set -e

COMMANDS=kind,kubectl,docker,vela
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -x

helm repo add kubevela https://charts.kubevela.net/core || yes
helm repo update
helm install --create-namespace -n vela-system kubevela kubevela/vela-core --set multicluster.enabled=true --wait
helm test kubevela -n vela-system

vela addon enable fluxcd
vela addon enable terraform
# vela addon enable observability alertmanager-pvc-enabled=false server-pvc-enabled=false grafana-domain=example.com