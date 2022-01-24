<h1 align="center">BairesDev News Project - Back-End</h1>
<h1 align="center">
    <a href="https://www.djangoproject.com/">🔗 Python/Django - Version</a>
</h1>



# Table of Contents

1. [About](#about)
2. [Installation](#installation)
3. [Running](#running)
4. [Endpoints](#endpoints)


## About

BairesDev News Project - Back-End

Since it is not a production version, the DEBUG option was not turned to FALSE.

## Installation

```bash
#Create a virtual environment on the current directory:
$ python3 -m venv path/to/new/virtual/environment
#Activate it:
$ source path/to/new/virtual/environment/activate/bin/activate
#Install the requirements
$ pip install -r requirements.txt
#Create migration files
$ python manage.py makemigrations api
#Run the migration files to create the database
$ python manage.py migrate
#(Optional)Call fetch_feed to import some data to the database
$ python manage.py fetch_feed
#(Optional)Create a pssword to access Django Admin
$ python manage.py createsuperuser
```

## Running

```bash
# Activate the virtual environment
$ source env/bin/activate
# Run the application
$ python3 manage.py runserver

Django admin can be accessed on: http://127.0.0.1:8000/admin
```

## Endpoints
- GET /api/entry:
Return one page of entries
- PATCH /api/entry/&ïd:
Update the click_count field from a specific ID 

