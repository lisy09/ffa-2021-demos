#!/bin/bash

PARENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROOT_DIR="$( cd $PARENT_DIR/.. >/dev/null 2>&1 && pwd )"
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

docker run \
    --name ${DNSMASQ_CONTAINER_NAME} \
    -d --rm \
    -p ${DNS_UDP_PORT}:53/udp \
    -p ${DNS_UI_PORT}:8080 \
    -v ${ROOT_DIR}/manifest/dnsmasq.conf:/etc/dnsmasq.conf \
    --log-opt "max-size=100m" \
    -e "HTTP_USER=admin" \
    -e "HTTP_PASS=123" \
    ${DNSMASQ_IMAGE_FULL}