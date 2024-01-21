# oroshine
oroshine

# Pre requisites

Python, virtual env and postgres DB must be installed .
Please follow following steps :

git clone git@github.com:devendrabobde/oroshine.git

cd oroshine

python3 -m venv env

source env/bin/activate

pip install django

django-admin startproject oroshine_app

cd oroshine_app/

pip install -r requirements.txt

python manage.py startapp oroshine_webapp

python manage.py runserver

pip install psycopg

python manage.py makemigrations

sudo -u postgres psql

Password for user postgres: 
psql (15.5 (Ubuntu 15.5-0ubuntu0.23.10.1), server 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# CREATE DATABASE oroshine;

postgres=# GRANT ALL PRIVILEGES ON DATABASE oroshine to postgres;

postgres=# \q


python manage.py migrate

python manage.py runserver

python manage.py createsuperuser {admin, admin@example.com, admin@123}

python manage.py runserver

### Run using docker compose

Make sure docker and docker compose is installed and update project directory in docker copose, and docker file and run bellow commands

Verify any images or containers are ruuning or not : docker ps -a;docker images -a

run app : sudo docker-compose up --build

Kill all images and containers : sudo docker-compose down -v ; sudo docker rm -vf $(sudo docker ps -aq) ; sudo docker rmi -f $(sudo docker images -aq)
