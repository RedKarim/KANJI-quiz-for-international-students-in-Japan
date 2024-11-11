#!/bin/bash

echo "Waiting for database..."
sleep 10

echo "Running migrations..."
python manage.py migrate

echo "Starting Django server..."
exec python manage.py runserver 0.0.0.0:8000 