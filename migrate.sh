#!/bin/bash
source .venv/bin/activate
yes | python manage.py makemigrations
#python manage.py migrate --fake
python manage.py migrate
git add post/migrations/*.py
git add users/migrations/*.py
git add receipts/migrations/*.py