#!/bin/bash
set -ex

python manage.py migrate --noinput
exec gunicorn pycon.wsgi:application
