FROM debian:jessie
MAINTAINER Jordi Riera <kender.jr@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install -y git wget libfreetype6 libfontconfig bzip2 libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev

# The pwd is not persistent across RUN commands. Need to cd and run commands over the
# same RUN.
RUN cd /tmp && \
    export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" && \
    wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 && \
    tar xvjf $PHANTOM_JS.tar.bz2 && \

    mv $PHANTOM_JS /usr/local/share && \
    ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

RUN apt-get install -y python python-pip
# to get --no-cache-dir option
RUN pip install pip --upgrade
ADD ./requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt --no-cache-dir

ENV PROJECT_HOME=/opt/crawler
RUN mkdir $PROJECT_HOME
WORKDIR $PROJECT_HOME