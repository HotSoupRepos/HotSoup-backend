FROM python:3.10-alpine

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./app/sample_locations.json /code/sample_locations.json 

RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]