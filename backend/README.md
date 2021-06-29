# Project Name

-- project description

## Getting on-board

### requirements for the project

1. Python >=v3.8.5
2. yarn v1.x
3. node
4. postgresql

### steps to init project

1. create and activate virtualenv `virtualenv env && source env/bin/activate`
2. run `pip3 install -r requirements.txt`
3. create .env from .env.example
4. run `yarn` to install node_modules
5. create postgres db named dyesee_db
6. run `python3 manage.py makemigrations`
7. run `python3 manage.py migrate`

### how to run project on localhost

1. run `python3 manage.py runserver` to start django server
2. run `python3 manage.py makemigrations` to make migrations
3. to create super user `python3 manage.py createsuperuser`
4. run `python3 manage.py migrate` to add migrations to db
5. run `yarn start` to start react server
