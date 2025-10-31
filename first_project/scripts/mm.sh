#!/bin/bash
cd azza && python manage.py makemigrations &&
sleep 0.5 && python manage.py migrate &&
python manage.py runserver
