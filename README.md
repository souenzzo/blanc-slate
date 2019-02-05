# Developer guide

First, be sure that you have [pipenv](https://github.com/pypa/pipenv) installed.
```bash
$ pipenv --version
pipenv, version 2018.11.15.dev0
```

Clone the project, then inside project dir
- Install the dependencies
```bash
$ pipenv sync
```
- Create the migrations for schedule
```bash
$ pipenv run python manage.py makemigrations schedule
```
- Create the SQLite database
```bash
$ pipenv run python manage.py migrate
```
- Create your first user
```bash
$ pipenv run python manage.py createsuperuser
```
- Run you server
```bash
$ pipenv run python manage.py runserver
```

Then you can connect in http://localhost:8000/admin
