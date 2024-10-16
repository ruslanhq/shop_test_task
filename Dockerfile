FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=src.config.settings.local

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python3 manage.py collectstatic

RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    chmod +x ./entrypoint.sh && \
    chown -R django:django /app

USER django

EXPOSE 8000
