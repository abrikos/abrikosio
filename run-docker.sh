#!/bin/bash
python -m venv .venv
source .venv/bin/activate
python manage.py makemigrations
#python manage.py migrate --fake
python manage.py migrate
python manage.py runserver 0.0.0.0:8000