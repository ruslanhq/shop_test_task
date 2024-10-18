#!/bin/sh

echo "Performing database migrations..."
python3 manage.py migrate

if ["$(python manage.py shell -c "from django.contrib.auth import get_user_model; print(get_user_model().objects.filter(is_superuser=True).exists())")" = "False"]; then
    echo "Creating superuser..."
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell
else
    echo "Superuser already exists"
fi

exec gunicorn src.config.wsgi:application --bind 0.0.0.0:8000
