#!/bin/bash
source .venv/bin/activate
python manage.py makemigrations
#python manage.py migrate --fake
python manage.py migrate
git add post/migrations/*.py
git add user/migrations/*.py