FROM python:3.11

WORKDIR /openclassrooms-p13

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ARG OC_LETTING_SENTRY_KEY
ARG OC_LETTING_SK

ENV OC_LETTING_SENTRY_KEY=$OC_LETTING_SENTRY_KEY
ENV OC_LETTING_SK=$OC_LETTING_SK
ENV DJANGO_DEBUG=0

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]