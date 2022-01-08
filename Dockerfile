FROM ubuntu:20.04

ENV TZ Canada/Eastern
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt upgrade -y && \
    apt install git -y && \
    apt install python3-pip -y

WORKDIR /home

COPY ./requirements.txt requirements.txt
RUN pip3 install -r requirements.txt