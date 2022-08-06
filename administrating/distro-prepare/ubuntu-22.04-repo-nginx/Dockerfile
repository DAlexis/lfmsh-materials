FROM ubuntu:22.04

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y nginx
COPY default /etc/nginx/sites-enabled/default

CMD ["nginx", "-g", "daemon off;"]

