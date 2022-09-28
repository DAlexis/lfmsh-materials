#!/bin/bash

cd /mnt/mirror/mirror
# cd /mnt/data-ext4-int/ubuntu-22.04-mirror/mirror
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy/main/dep11/
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy/main/cnf
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy/universe/dep11/
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy/universe/cnf

wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy/restricted/cnf

wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy-updates/main/dep11/
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy-updates/main/cnf
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy-updates/universe/dep11/
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy-updates/universe/cnf
wget --no-parent --recursive http://ru.archive.ubuntu.com/ubuntu/dists/jammy-updates/restricted/cnf
