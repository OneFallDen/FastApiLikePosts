FROM python:3.11.3

ENV PYTHONUNBUFFERED=1

RUN apt update && apt -y install gcc libpq-dev

RUN pip install --upgrade pip

RUN pip install poetry
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

COPY . /app

RUN poetry install

ENTRYPOINT ["poetry", "run"]
EXPOSE 8000
