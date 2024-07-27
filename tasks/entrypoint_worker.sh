#!/bin/sh

# Применить и создать миграции
python manage.py migrate --noinput

# Запуск Celery worker
celery -A core worker --loglevel=info
