FROM python:3.12-slim-bullseye as build-image

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.8.2

ENV PYTHONPATH=/app

ARG RELEASE_VERSION=0.0.0
ENV RELEASE=$RELEASE_VERSION

RUN pip install poetry
RUN pip install poetry-plugin-bundle
RUN apt update && apt install gcc -y

WORKDIR /app
COPY pyproject.toml poetry.lock README.md ./

#RUN poetry config virtualenvs.create false && \
#    poetry install --without=dev --no-interaction --no-ansi
RUN poetry bundle venv --python=/usr/local/bin/python3 --only=main /venv

FROM python:3.12-alpine as runtime-image

COPY --from=build-image /usr/local /usr/local

WORKDIR /app
COPY --from=build-image /venv /venv
COPY pyproject.toml poetry.lock ./

COPY docker/gunicorn_conf.py /gunicorn_conf.py
COPY ./app /app/app

CMD ["/venv/bin/gunicorn", "-k uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "app.main:app"]


#RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
#
#RUN chown -R nonroot:nonroot /app
#RUN chown -R nonroot:nonroot /usr/local
#RUN chown -R nonroot:nonroot /gunicorn_conf.py
#
#USER nonroot
