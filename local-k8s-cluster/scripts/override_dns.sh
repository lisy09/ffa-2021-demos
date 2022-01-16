#!/usr/bin/env bash

readonly SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
source $ROOT_DIR/.env

set -e
set -x

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)    machine=Linux;;
    Darwin*)   machine=Mac;;
    *)         machine="UNKNOWN:${unameOut}"
esac
echo "Running on machine: ${machine}"

if [ "$machine" = "Mac" ]; then
    brew install dnsmasq
    echo bind-interfaces > /usr/local/etc/dnsmasq.conf
    echo listen-address=127.0.0.1 >> /usr/local/etc/dnsmasq.conf
    echo address=/.localhost/127.0.0.1 >> /usr/local/etc/dnsmasq.conf
    sudo brew services start dnsmasq
    sudo mkdir -p /etc/resolver/
    sudo bash -c "echo 'nameserver 127.0.0.1' > /etc/resolver/dnsmasq"
else
    sudo apt-get install dnsmasq
    sudo bash -c "echo conf-dir=/etc/dnsmasq.d/,*.conf >> /etc/dnsmasq.conf"
    sudo bash -c "echo address=/.localhost/127.0.0.1 > /etc/dnsmasq.d/localhost"
    sudo bash -c "echo nameserver 127.0.0.1 >> /etc/resolv.conf"
    sudo service dnsmasq restart
fi