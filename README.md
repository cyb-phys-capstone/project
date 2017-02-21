# Cyberphysical Simulation Project
Authors:
Mohit Mehrotra, Aaron Lajom, Sean Scott, Carlos Davila, Eric Reeves

# Database Setup
**Requires [PostgreSQL](https://www.postgresql.org/download/), [pgAdmin](https://www.pgadmin.org/download/), and [Anaconda for Python 3](https://www.continuum.io/downloads)**

Run the following commands in your terminal:

`pip install -r requirements.txt`

`conda install psycopg2`

Install [Redis].
Make sure it's running with:
```sh
\>redis-cli ping
PONG <----what you should see
```


Use the fields in the `DATABASES` block of [settings.py](CYB_PHYS_CAPSTONE/CYB_PHYS_CAPSTONE/settings.py) to fill in the following placeholders:
- In pgAdmin, create a PostgreSQL server (if none exist) on $PORT. The default username and password will be fine. Host = localhost.
- Create a new login role for the $USER, with $PASSWORD
- Create a new database, where Name = $NAME, Owner = $USER

`cd` into the project directory, where `manage.py` is located. Set up the database by running:
`python manage.py migrate`

Start the celery worker service via:

`celery -A CYB_PHYS_CAPSTONE worker -l info`

Start the celery beat service for periodic background tasks with:

`celery -A CYB_PHYS_CAPSTONE beat -l info -S django`

And then run the server (separate terminal) via:

`python manage.py runserver`

You can now view the database on [localhost:8000](http://localhost:8000)!

When models are updated, refresh the database by running:

`python manage.py makemigrations`

`python manage.py migrate`
