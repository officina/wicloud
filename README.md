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

 - virtualenvwrapper (suggested :
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


## Install the requirements

```
pip install .
```

## Create the database

```
createdb wicloud
```

or

```
docker-compose -f docker/postgres/postgres.yml up -d
dj migrate
```

## Link settings.py with the desired configuration
```
ln -s "$(pwd)/web/settings/dev.py" "$(pwd)/web/settings/settings.py" ```
## Create local.py file inside web/settings
```

```
vi web/settings/local.py
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

# Launch the angular frontend (in another pycharm terminal tab):

```
cd angular
yarn install
yarn start
```
# Have fun!


# Check lint before push

    npm run -s prepush

    npm run lint:ci && ng build --prod

    ng lint

    ./node_modules/stylelint/bin/stylelint.js ./src/**/*.scss
    
# Build for production

     ng build --prod
     
In case of error 

```FATAL ERROR: Ineffective mark-compacts near heap limit Allocation failed - JavaScript heap out of memory```

Increase the Node memory

    npm install -g increase-memory-limit

    increase-memory-limit

     /usr/local/Cellar/node/9.8.0/lib/node_modules/increase-memory-limit/index.js
 
# If the production build fails because of memory issues
https://geeklearning.io/angular-aot-webpack-memory-trick/

    npm install -g increase-memory-limit

and then in the project folder execute

    increase-memory-limit
or

    /usr/local/Cellar/node/9.8.0/lib/node_modules/increase-memory-limit/index.js

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


# Elastic Search

Per creare gli indici delle entità

    ./manage.py search_index --create -f 
    
Per popolare gli indici

    manage.py search_index --populate -f 
    
Per ricostruire gli indici

    manage.py search_index --rebuild
    
Esempi di query

    http://localhost:8000/api/search/installations/?ids=1__3
    
    http://localhost:8000/api/search/installations/?notes__wildcard=*tata
    
    localhost:8000/api/search/installations/?search=name:Seconda
    
    localhost:8000/api/search/installations/?search=banana
    
    localhost:8000/api/search/installations/?search=patata



##Backup with structure
pg_dump --user wilampcloud --host localhost --dbname=wicloud --file="/Users/andrea/dump.sql" 

##Backup without structure

###Con copy (+ veloce e compatto)
pg_dump --user wilampcloud --host localhost --dbname=wilampcloud --file="/Users/andrea/dump.sql" --data-only


###Con copy selettivo
pg_dump --user wilampcloud --host localhost --data-only --dbname=wilampcloud --schema='public'    --table=public.address --table=public.contact --table=public."contact_address" --table=public.customer --table=public."customer_users" --table=public.installation --table=public.gateway --table=public."energy_interval" --table=public."energy_meter_module" --table=public."energy_meter_peak_measure" --table=public."gateway_config" --table=public."gateway_installation_request"  --table=public."last_energy_interval" --table=public."light_management_module" --table=public."light_management_measure"  --table=public."lm_measure_processing_info" --table=public."log_entry" --table=public."motion_event" --table=public."motion_management_module" --table=public."node_modules" --table=public.node  --table=public.shipping --table=public."shipping_order" --table=public."twilight_management_module" --table=public."twilight_measure" --table=public."vpn_configuration" --table=public."ime_power_counter" --table=public."ime_power_measure" --file="./dump.sql"

###Con insert
pg_dump --user wilampcloud --host localhost --dbname=wilampcloud --file="/Users/andrea/dump.sql" --column-inserts --data-only

##Restore
psql  --host localhost --user wilampcloud --file="/Users/andrea/dump.sql" 

