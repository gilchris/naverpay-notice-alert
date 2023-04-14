FROM python:3.10-alpine

COPY naverpay_notice_parser.py .
COPY __init__.py .
COPY requirements.txt .

RUN pip install -r ./requirements.txt

CMD python3 ./__init__.py