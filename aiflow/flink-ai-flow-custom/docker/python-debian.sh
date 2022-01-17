#!/usr/bin/env bash

export PIPX_HOME=${1:-"/usr/local/py-utils"}
USERNAME=${2:-"automatic"}

set -e

DEFAULT_UTILS="\
    pylint \
    flake8 \
    autopep8 \
    black \
    yapf \
    mypy \
    pydocstyle \
    pycodestyle \
    bandit \
    pipenv \
    virtualenv"


export PIPX_BIN_DIR=${PIPX_HOME}/bin
export PATH=${PYTHON_INSTALL_PATH}/bin:${PIPX_BIN_DIR}:${PATH}

# Update pip
echo "Updating pip..."
python3 -m pip install --no-cache-dir --upgrade pip

# Create pipx group, dir, and set sticky bit
if ! cat /etc/group | grep -e "^pipx:" > /dev/null 2>&1; then
    groupadd -r pipx
fi
usermod -a -G pipx ${USERNAME}
umask 0002
mkdir -p ${PIPX_BIN_DIR}
chown :pipx ${PIPX_HOME} ${PIPX_BIN_DIR}
chmod g+s ${PIPX_HOME} ${PIPX_BIN_DIR}

# Install tools
echo "Installing Python tools..."
export PYTHONUSERBASE=/tmp/pip-tmp
export PIP_CACHE_DIR=/tmp/pip-tmp/cache
pip3 install --disable-pip-version-check --no-warn-script-location  --no-cache-dir --user pipx
/tmp/pip-tmp/bin/pipx install --pip-args=--no-cache-dir pipx
echo "${DEFAULT_UTILS}" | xargs -n 1 /tmp/pip-tmp/bin/pipx install --system-site-packages --pip-args '--no-cache-dir --force-reinstall'
rm -rf /tmp/pip-tmp