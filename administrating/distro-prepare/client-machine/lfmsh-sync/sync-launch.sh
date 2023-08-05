#/bin/bash


if [[ $(ps axo user:20,command | grep sync-infinite | grep ${USER} | grep -v grep) ]]; then
    echo "Process already runs by user ${USER}"
else
    /opt/lfmsh-sync/sync-infinite.sh
fi


