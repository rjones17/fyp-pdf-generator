# Base Image
FROM python:3.8-slim-buster

# ENV Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

# Image Dependencies
RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Work Dir
WORKDIR /app

# Dependencies
COPY Pipfile Pipfile.lock /
RUN pip install pipenv && pipenv install --dev --system

