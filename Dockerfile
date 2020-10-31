FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip sudo ffmpeg libsm6 libxext6

RUN pip3 install --upgrade pip

RUN useradd -m dhruv

RUN chown -R dhruv:dhruv /home/dhruv/

COPY --chown=dhruv . /home/dhruv/app/

USER dhruv

RUN cd /home/dhruv/app/ && pip3 install -r requirements.txt

WORKDIR /home/dhruv/app

CMD python3 main.py
