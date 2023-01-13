FROM python:3.8.0-slim

RUN mkdir /app

WORKDIR /app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY requirements.txt /app/

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade setuptools

RUN pip3 install -r requirements.txt

COPY . /app/
