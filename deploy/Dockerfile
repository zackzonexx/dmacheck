FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN apk update && \
    apk add --update curl && \
    apk add python3-dev gcc build-base && \
    apk add --no-cache bash git make && \
    rm -rf /var/cache/apk/*

RUN pip3 install -r requirements.txt
RUN pip3 list
