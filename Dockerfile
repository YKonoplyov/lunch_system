FROM python:3.11-alpine3.18
LABEL maintainer="kannabis252@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR lunch_system/

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password\
    --no-create-home\
    django-user


USER django-user