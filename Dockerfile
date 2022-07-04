FROM python:3.10-alpine

ENV POETRY_VERSION=1.1.13

RUN pip install poetry==${POETRY_VERSION}

WORKDIR /code

COPY poetry.lock pyproject.toml /code/


#Turn off virtual env since it will be in a container.
RUN poetry config virtualenvs.create false 
#install all dependancies via poetry.lock and pyproject.toml
RUN poetry install

COPY ./app /code/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]