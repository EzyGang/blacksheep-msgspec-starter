FROM python:3.12-alpine as compile-image

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.2

ENV PYTHONPATH=/app

RUN pip install poetry
RUN apk add gcc python3-dev libc-dev

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --without=dev --no-interaction --no-ansi --no-cache

RUN pip uninstall poetry -y
RUN apk del gcc python3-dev libc-dev


FROM python:3.12-alpine as runtime-image

COPY --from=compile-image /usr/local /usr/local

ENV PYTHONPATH=/app
WORKDIR /app

ARG RELEASE_VERSION=0.0.0
ENV RELEASE=$RELEASE_VERSION

COPY docker/gunicorn_conf.py /gunicorn_conf.py
COPY ./app /app/app

CMD ["gunicorn", "-k uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "app.main:app"]

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot

USER nonroot
