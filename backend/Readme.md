# create venv
`virtualenv venv`

# activate venv
`source venv/bin/activate`

# install locally
`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py add_users`

Mac, Linux:
`python manage.py loaddata data/master-data/*.json`
`python manage.py loaddata data/test-data/*.json`

Windows: `python manage.py add_fixtures test-data`

`python manage.py runserver`

# deactivate venv
`deactivate`

# PostGres for MacOS
`brew install postgresql`


# install aws
`get zappa_settings.json from Hagi or Robert`
`zappa update dev (or prod)`

