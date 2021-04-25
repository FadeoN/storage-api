FROM python:3.7-slim

COPY requirements.txt /

RUN python3 -m pip install -r requirements.txt

COPY . /storage-api

WORKDIR /storage-api

ADD . /storage-api

EXPOSE 5002

CMD ["python3", "main.py"]