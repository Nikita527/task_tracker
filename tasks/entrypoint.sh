#!/bin/sh

# Применить и создать миграции
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Собрать статические файлы
python manage.py collectstatic --noinput

# Запуск Gunicorn
gunicorn --bind 0.0.0.0:8000 core.wsgi:application
