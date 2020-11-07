# Base Image
FROM python:3.8

# ENV Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

# Work Dir
WORKDIR /code/

# Dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# COPY
COPY . /code/