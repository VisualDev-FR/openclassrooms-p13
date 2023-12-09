FROM python:3.11.6-slim

WORKDIR /app

COPY . .

VOLUME [ "/app" ]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "sh", "entrypoint.sh" ]