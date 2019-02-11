FROM python:3.6.7

MAINTAINER Max Korsun

RUN apt-get update

RUN mkdir -p /usr/src/myapp

WORKDIR /usr/src/myapp

COPY requirements.txt /usr/src/myapp/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/src/myapp/

CMD ["python3", "run.py"]