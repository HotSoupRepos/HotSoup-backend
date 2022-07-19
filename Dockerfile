FROM python:3.10-slim

ENV POETRY_VERSION=1.1.13

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /code

COPY poetry.lock pyproject.toml /code/
COPY ./app/data.json /code/data.json
#TODO - line 10 above is a dummy data file for testing, remove when db is seeded/integrated

#Turn off virtual env since it will be in a container.
RUN poetry config virtualenvs.create false 
#install all dependencies via poetry.lock and pyproject.toml
RUN poetry install

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
