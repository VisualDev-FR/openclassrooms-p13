FROM python:3.11.6-slim

WORKDIR /app

COPY . .

VOLUME [ "/app" ]

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ARG OC_LETTING_SENTRY_KEY
ARG OC_LETTING_SK

ENV OC_LETTING_SENTRY_KEY=$OC_LETTING_SENTRY_KEY
ENV OC_LETTING_SK=$OC_LETTING_SK
ENV DJANGO_DEBUG=0

RUN python manage.py collectstatic --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
