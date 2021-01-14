FROM mysql:5.7

WORKDIR /db

RUN apt-get update \
    && apt-get install -y wget \
    && wget --no-check-certificate "https://onedrive.live.com/download?cid=613ED828EACCABDA&resid=613ED828EACCABDA%21157398&authkey=AEny8hVkXyL0ubc" -O users.csv

COPY init/ /docker-entrypoint-initdb.d/