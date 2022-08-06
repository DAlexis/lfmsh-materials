#!/bin/bash

docker run -it --rm \
  --mount type=bind,source=/mnt/data-ext4-int/ubuntu-22.04-mirror,target=/srv/http \
  -p 80:80 \
  ubuntu-mirror-nginx
