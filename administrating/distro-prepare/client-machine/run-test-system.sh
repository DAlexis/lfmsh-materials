#!/bin/bash

docker run -it --rm \
  --log-driver none \
  ubuntu-lfmsh-test
# --volume /etc/passwd:/etc/passwd:ro -v /etc/group:/etc/group:ro \
#--user $(id -u):$(id -g) \
