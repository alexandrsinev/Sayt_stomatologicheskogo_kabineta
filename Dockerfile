FROM python:3.12-slim

WORKDIR /code

RUN pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .