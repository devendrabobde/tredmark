# tredmark
tredmark

# Pre requisites

Python, virtual env and postgres DB must be installed

git clone git@github.com:devendrabobde/tredmark.git
cd tredmark
python3 -m venv env
source env/bin/activate
pip install django
django-admin startproject tredmark_app
cd tredmark_app/
python manage.py startapp tredmark_webapp
python manage.py runserver
pip install psycopg
python manage.py makemigrations

sudo -u postgres psql

Password for user postgres: 
psql (15.5 (Ubuntu 15.5-0ubuntu0.23.10.1), server 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# CREATE DATABASE tredmark;
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE tredmark to postgres;
GRANT
postgres=# \q


python manage.py migrate
python manage.py runserver
python manage.py createsuperuser {admin, admin@example.com, admin@123}
python manage.py runserver
