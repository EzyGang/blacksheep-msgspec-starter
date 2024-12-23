FROM ghcr.io/astral-sh/uv:python3.12-alpine AS compile-image

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV UV_PROJECT_ENVIRONMENT="/venv" \
    UV_COMPILE_BYTECODE=1 \
    UV_FROZEN=1

ENV PYTHONPATH=/app

RUN apk add gcc python3-dev libc-dev

WORKDIR /app
COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev

# Runtime iamge
FROM python:3.12-alpine AS runtime-image


ENV UV_PROJECT_ENVIRONMENT="/venv" \
    UV_COMPILE_BYTECODE=1 \
    UV_FROZEN=1

ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH" \
    PATH="/venv/bin:$PATH" \
    PYTHONPATH=/app

WORKDIR /app

ARG RELEASE_VERSION=0.0.0
ENV RELEASE=$RELEASE_VERSION

# Copy source and venv
COPY pyproject.toml uv.lock ./
COPY ./app /app/app
COPY ./docker/gunicorn_conf.py /gunicorn_conf.py
COPY --from=compile-image /venv /venv

CMD ["gunicorn", "-k uvicorn.workers.UvicornWorker", "-c", "/gunicorn_conf.py", "app.main:app"]

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot && \
    chown -R nonroot:nonroot /usr/local && \
    chown -R nonroot:nonroot /venv && \
    chown -R nonroot:nonroot /app

USER nonroot
