#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000