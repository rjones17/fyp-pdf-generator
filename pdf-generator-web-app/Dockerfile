# Base Image
FROM python:3.8

# ENV Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

# Work Dir
RUN mkdir /src
WORKDIR /src

# Dependencies
COPY Pipfile Pipfile.lock /src/
RUN pip install pipenv && pipenv install --system

# COPY
COPY ./src /src