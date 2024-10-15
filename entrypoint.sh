#!/bin/sh

echo "Performing database migrations..."
python3 manage.py migrate

echo "Creating superuser..."
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

exec gunicorn src.config.wsgi:application --bind 0.0.0.0:8000
