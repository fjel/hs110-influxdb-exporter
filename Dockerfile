#Python3
FROM python:3-alpine

RUN mkdir /kasa-exporter
WORKDIR /kasa-exporter

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY hs110-exporter.py .
CMD ["python", "hs110-exporter.py"]