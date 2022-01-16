#!/bin/bash

PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR="$( cd $PARENT_DIR/.. >/dev/null 2>&1 && pwd )"
MANIFEST_DIR=$ROOT_DIR/manifest

source $ROOT_DIR/.env
set -e

COMMANDS=docker
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -x

# create a nfs server with docker
rm -rf ${ROOT_DIR}/${NFS_DATA_DIR}
mkdir -p ${ROOT_DIR}/${NFS_DATA_DIR}
docker run -d --rm \
    --name ${NFS_CONTAINER_NAME} \
    --cap-add SYS_ADMIN \
    -v ${ROOT_DIR}/${NFS_DATA_DIR}:/nfs/data \
    -e SHARED_DIRECTORY=/nfs/data \
    -p ${NFS_SERVER_PORT}:2049 \
    ${NFS_IMAGE_FULL}

# setup nfs storage class
mkdir -p ${ROOT_DIR}/${NFS_DATA_DIR}/k8s_nfs
kubectl apply -f ${MANIFEST_DIR}/nfs.yaml
kubectl wait --namespace default \
    --for=condition=ready pod \
    --selector=app=nfs-client-provisioner \
    --timeout=90s