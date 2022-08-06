FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y apt-mirror apt-utils
WORKDIR /app
COPY mirror.list /etc/apt/mirror.list
COPY download-missing.sh .

CMD ["/bin/bash"]

