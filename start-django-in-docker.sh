#!/bin/bash
#pip install -r requirements.txt
#python manage.py migrate --fake
rm -fr /app/docker_volumes/static/*
cp -r /app/bundle/* /app/docker_volumes/static/

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000