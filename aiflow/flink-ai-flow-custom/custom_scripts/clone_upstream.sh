#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

usage() {
  echo -n "Usage: ${0} " >&2
  echo -n "--branch BRANCH (git branch to be clone for ai-flow) " >&2
  echo >&2
}

COMMANDS=git
IFS=',' read -a commands <<< ${COMMANDS}
for COMMAND in ${commands[@]}; do
    if ! command -v ${COMMAND} &> /dev/null; then
        echo "Command could not be found: ${COMMAND}"
        exit 1
    fi
done

while [[ ${#} -gt 0 ]]; do
  parameter="${1}"

  case "${parameter}" in
    --branch|-b)
      branch="${2}"
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

for parameter in branch; do
  if [[ -z ${!parameter} ]]; then
    echo "Missing ${parameter}" >&2
    echo >&2
    usage
    exit 1
  fi
done

echo "Cloning branch: $branch ..."

if [ -z "${TEMP_CLONE_ROOT_DIR}" ]; then
  echo "TEMP_CLONE_ROOT_DIR should be set in env!"
  exit 1
fi

readonly CLONE_ROOT_DIR=$ROOT_DIR/$TEMP_CLONE_ROOT_DIR
rm -rf $CLONE_ROOT_DIR
git clone --depth 1 --branch $branch $UPSTREAM_REPO $CLONE_ROOT_DIR