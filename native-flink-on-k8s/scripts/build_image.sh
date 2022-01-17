#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"


image_prefix=

usage() {
  echo -n "Usage: ${0} " >&2
  echo -n "--prefix|-p IMAGE_PREFIX " >&2
  echo >&2
}

while [[ ${#} -gt 0 ]]; do
  parameter="${1}"

  case "${parameter}" in
    --prefix|-p)
      image_prefix="${2}"
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Invalid parameter: ${parameter}" >&2
      exit 1
      ;;
  esac

  shift
done

for parameter in image_prefix; do
  if [[ -z ${!parameter} ]]; then
    echo "Missing ${parameter}" >&2
    echo >&2
    usage
    exit 1
  fi
done

source $ROOT_DIR/.env

COMMANDS=docker
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

set -e
set -x

PREFIX=${image_prefix}

VAR_BUILD_ARGS=${PREFIX}_BUILD_ARGS
IFS=',' read -a _build_args <<< ${!VAR_BUILD_ARGS}
build_args=
for BUILD_ARG in ${_build_args[@]}; do
    build_args+=" --build-arg ${BUILD_ARG}"
done

VAR_IMAGE_FULL=${PREFIX}_IMAGE_FULL
VAR_DOCKERFILE=${PREFIX}_DOCKERFILE
VAR_CONTEXT=${PREFIX}_CONTEXT
docker build ${build_args} \
    -t ${!VAR_IMAGE_FULL} \
    -f $ROOT_DIR/${!VAR_DOCKERFILE} \
    $ROOT_DIR/${!VAR_CONTEXT}