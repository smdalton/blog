#!/usr/bin/env bash

rm -f db.sqlite3
rm -r techblog/migrations
cd techblog
mkdir migrations
cd migrations
touch __init__.py
cd ..
cd ..
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db