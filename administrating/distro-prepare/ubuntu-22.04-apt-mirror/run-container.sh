#!/bin/bash

docker run -it --rm \
  --mount type=bind,source=/mnt/data-ext4-int/ubuntu-22.04-mirror,target=/mnt/mirror \
  --user $(id -u):$(id -g) \
  --log-driver none \
  --volume /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
  ubuntu-apt-mirror
