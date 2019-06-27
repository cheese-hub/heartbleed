FROM dorowu/ubuntu-desktop-lxde-vnc:bionic

MAINTAINER Rajesh Kalyanam "rkalyanapurdue@gmail.com"

#create a non-root user
RUN useradd -d /home/victim -m -s /bin/bash victim

RUN echo 'victim:victim' | chpasswd

ENV USER=victim \
    PASSWORD=victim 

