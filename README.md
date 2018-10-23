# wicloud

## Clone the respository
```
git clone ssh://github.com/officina/wicloud
```

## Use Virtualenv and Virtualenvwrapper

The [virtualenv](https://virtualenv.pypa.io/en/stable/), put simply, is an isolated working copy of Python which
allows you to work on a specific project without worry of affecting other projects. It enables multiple side-by-side installations of Python, one for each project. It doesn’t actually install separate copies of Python, but it does provide a clever way to keep different project environments isolated.

[Virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) is a set of extensions to virtualenv. It gives you commands like mkvirtualenv, lssitepackages, and especially workon for switching between different virtualenv directories. This tool is especially useful if you want multiple virtualenv directories.

### Installation

```
pip install --user virtualenv virtualenvwrapper
```

### Configuration

Add three lines to your shell startup file (.bashrc, .profile, etc.) to set the location where the virtual environments should live, the location of your development project directories, and the location of the script installed with this package:

```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Workspace
source /usr/local/bin/virtualenvwrapper.sh
```

### Create and activate the virtual environment


####Create virtualenv:

 - virtualenv (standard):
     - python3:

        `virtualenv wicloud/venv --python /usr/bin/python3`

 - virtualenvwrapper:
    - python3:

        `mkvirtualenv --python=/usr/bin/python3 wicloud`

 - Python3 Venv (only for python 3):

    `python3 -m venv wicloud/venv`


####Activate virtualenv:

- virtualenv (standard) & Python3 Venv (only for python 3):

    `. venv/bin/activate`

- virtualenvwrapper:
    `workon wicloud`

## Install and configure autoenv

Cookiecutter prepare automatically `.env` file, but is necessary install the *global* package

```
sudo pip install autoenv
```

and configure your `.bashrc`:
```
echo "source `which activate.sh`" >> ~/.bashrc
```
For create autoenv in your project (in this example with virtualenvwrapper) create `.env` file as follows:
```
echo "workon wicloud" > .env
```

The complete autoenv documentation can be found [here](https://github.com/kennethreitz/autoenv).



## Configure pip for Thux pypi

Any package are developed internal in Thux, to automataically check correct repo cretate `.pip/pip.conf`:
```
[global]
find-links = https://pypi.thux.it/
```

## Install the requirements

```
pip install .
```

## Create the database

```
createdb wicloud
```
## Create local.py file inside web/settings

```
gedit web/settings/local.py
```
## Copy the following settings into the local.py file

```
#!python

# -*- coding: utf-8 -*-
SECRET_KEY = 'Place your brand new security key here'
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wicloud',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
EMAIL_SUBJECT_PREFIX = ['wicloud']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## Apply Migrations

```
dj migrate
```

## Create admin account

```
dj createsuperuser
```

## Create static folder inside web dir

```
cd wicloud/web
mkdir static

```

## Run django server

```
dj r
```

# Have fun!

# Remote tests

```
 from web.remote_test import RemoteTest
 rt = RemoteTest('localhost') #host opzionale 
 rt.login('admin', 'password)
 rt.backend_wicloud_address_list()
 In [5]: rt.backend_wicloud_address_list()
'http://127.0.0.1:8000/wicloud/api/address/list/'
200
'OK'
{'count': 1,
 'current': 1,
 'first': 1,
 'first_link': 'http://127.0.0.1:8000/wicloud/api/address/list/?page=1',
 'last': 1,
 'last_link': 'http://127.0.0.1:8000/wicloud/api/address/list/?page=1',
 'next': None,
 'next_link': None,
 'per_page': 10,
 'previous': None,
 'previous_link': None,
 'results': [{'address_description': 'Via roma',
              'city': 'Padova',
              'country': 'Italia',
              'creator': 1,
              'created_date': '2018-09-27T23:13:48.049347',
              'last_modified_date': '2018-09-28T12:47:57.183959',
              'full_name': 'Maschio Andrea',
              'house_number': 'lkj',
              'id': 1,
              'last_modifier': 1,
              'lat': '45',
              'lng': '11',
              'ordering': 0,
              'status': 1,
              'street': 'Via Roma',
              'timezone_code': 'CET',
              'zip_code': '35143'}]}

Out[5]: <Response [200]>

```
