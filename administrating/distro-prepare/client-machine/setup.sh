#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: setup.sh SERVER_IP" >&2
    exit 1
fi

SERVER_IP="$1"

set -e

# quietly add a user without password
sudo adduser --quiet --disabled-password --shell /bin/bash --home /home/pioner --gecos "Pioner" pioner

# set password
echo "pioner:voyager" | sudo chpasswd

cat sources.list | sed s/SERVER_IP/${SERVER_IP}/ > sources.list.patched
cat pip.conf | sed s/SERVER_IP/${SERVER_IP}/ > pip.conf.patched

sudo cp /etc/apt/sources.list /etc/apt/sources.list.default
sudo cp sources.list.patched /etc/apt/sources.list
sudo apt-get update -y
sudo apt-get upgrade -y
#sudo apt-get install -y --allow-unauthenticated g++ qtcreator python3-venv python3-pip openssh-server syncthing htop mc cmake qtcreator git gimp
sudo apt-get install -y --allow-unauthenticated python3-venv python3-pip

sudo mkdir -p /home/pioner/.config/pip/
sudo cp pip.conf.patched /home/pioner/.config/pip/pip.conf
sudo chown -R pioner:pioner /home/pioner/.config

sudo su pioner <<EOSU
mkdir -p /home/pioner/.config/pip/
cp pip.conf.patched /home/pioner/.config/pip/pip.conf
EOSU


