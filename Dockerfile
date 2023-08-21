FROM python:3.11.4-bullseye

WORKDIR /code

COPY . .

RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
