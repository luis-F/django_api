FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
  ca-certificates gcc postgresql-dev linux-headers musl-dev \
  libffi-dev jpeg-dev zlib-dev bash

RUN pip install --upgrade pip
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN mkdir -p /api
COPY . /api
