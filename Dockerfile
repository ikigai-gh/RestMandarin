FROM python:3.6-slim

WORKDIR /rest_mandarin

COPY . /rest_mandarin

RUN pip install -r requirements.txt

EXPOSE 8000

CMD gunicorn rest_api:api

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "rest_api:api"]
