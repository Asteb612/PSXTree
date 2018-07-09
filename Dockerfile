FROM python:3.6
LABEL maintainer "Arthur Grosso <arthur.grosso@epitech.eu>"
RUN apt-get update
RUN mkdir /psxtree
WORKDIR /psxtree
COPY . /psxtree
RUN pip install --no-cache-dir -r requirements.txt
