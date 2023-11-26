FROM python:3

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . .
