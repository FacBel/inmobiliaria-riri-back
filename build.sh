#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd src
python manage.py collectstatic --no-input
python manage.py migrate

# Crea el superusuario con las variables DJANGO_SUPERUSER_* de Render
python manage.py createsuperuser --noinput || true
