#!/bin/bash

source source .venv/bin/activate
exec gunicorn --bind 0.0.0.0:10000 --workers 4 quiz_gen_django.wsgi:application
