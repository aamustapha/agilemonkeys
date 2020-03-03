FROM python:3.7-alpine
MAINTAINER Abdulhakeem Mustapha

ENV PYTHONUNBUFFERED 1

RUN apk update
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /code
WORKDIR /code
COPY ./ /code

RUN adduser -D user
USER user
