FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y sudo

RUN useradd -ms /bin/bash administrator && echo "administrator:noway" | chpasswd && adduser administrator sudo
USER administrator
WORKDIR /home/administrator

COPY sources.list .
COPY pip.conf .
COPY setup.sh .

