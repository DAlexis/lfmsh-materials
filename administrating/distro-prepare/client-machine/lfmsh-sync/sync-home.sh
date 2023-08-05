#!/bin/bash

set -e

cd ${HOME}

SYNC_VERSION_FILE=.lfmsh_syncversion
TEMP_DIR=${HOME}/.lfmsh_synctemp

EXCLUDE_LINE="--exclude .Xauthority --exclude .face --exclude .cache --exclude .xsession-errors --exclude *.pid --exclude .config --exclude .local --exclude .kde --exclude .lfmsh_synctemp --exclude .ssh"

mkdir -p ${TEMP_DIR}
scp homesync@SERVER_IP:${USER}/${SYNC_VERSION_FILE} ${TEMP_DIR} || echo "-1" > ${TEMP_DIR}/${SYNC_VERSION_FILE}
local_version=`cat ${HOME}/${SYNC_VERSION_FILE}`
remote_version=`cat ${TEMP_DIR}/${SYNC_VERSION_FILE}`

if (( $remote_version > $local_version )); then
    echo "remote version grater"
    rsync -avz --delete --timeout=60 --max-size=100m ${EXCLUDE_LINE} homesync@SERVER_IP:${USER}/ ~ 2>&1 >> ~/sync-pull.log
    exit 0
fi

if (( $local_version == $remote_version )); then
    echo "remote version equals local"
    new_version=$((local_version + 1))
    local_version=$new_version
    echo $new_version > $SYNC_VERSION_FILE
fi

rsync -avz --delete --timeout=60 --max-size=100m ${EXCLUDE_LINE} ~ homesync@SERVER_IP: 2>&1 >> ~/sync-push.log
