#!/bin/sh

echo "Performing database migrations..."
python3 manage.py migrate

if [ -z "$(echo "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())" | python manage.py shell)" ]; then
    echo "Creating superuser..."
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
else
    echo "Superuser already exists"
fi

exec gunicorn src.config.wsgi:application --bind 0.0.0.0:8000
