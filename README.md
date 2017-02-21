# Cyberphysical Simulation Project
Authors:
Mohit Mehrotra, Aaron Lajom, Sean Scott, Carlos Davila, Eric Reeves

# Database Dependencies (Raspberry Pi)
**Requires [PostgreSQL](https://www.postgresql.org/download/), [pgAdmin](https://www.pgadmin.org/download/), and [Minconda](http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-armv7l.sh)**

Install the libpq package with;

`sudo apt-get install libpq-dev`

Install Psycopg2 from source via https://pypi.python.org/pypi/psycopg2#downloads

# Database Dependencies (Windows/Linux)
**Requires [PostgreSQL](https://www.postgresql.org/download/), [pgAdmin](https://www.pgadmin.org/download/), and [Anaconda for Python 3](https://www.continuum.io/downloads)**

Install Psycopg2 via command line:

`conda install psycopg2`

# Setup

Run the following commands in your terminal:

`pip install -r requirements.txt`

Use the fields in the `DATABASES` block of [settings.py](CYB_PHYS_CAPSTONE/CYB_PHYS_CAPSTONE/settings.py) to fill in the following placeholders:
- In pgAdmin, create a PostgreSQL server (if none exist) on $PORT. The default username and password will be fine. Host = localhost.
- Create a new login role for the $USER, with $PASSWORD
- Create a new database, where Name = $NAME, Owner = $USER

`cd` into the project directory, where `manage.py` is located. Set up the database by running:

`python manage.py migrate`

And then run the server via:

`python manage.py runserver`

You can now view the database on [localhost:8000](http://localhost:8000)!

When models are updated, refresh the database by running:

`python manage.py makemigrations`

`python manage.py migrate`

# Celery
[Celery](http://www.celeryproject.org/) is a service that enables tasks to be run periodically without the need for user interaction. All the necessary dependencies are installed via [requirements.txt](CYB_PHYS_CAPSTONE/requirements.txt).

Celery is used for scraping NREL data every 30 minutes. Via the Django Admin page, a Periodic Task can be created.

Celery requires Redis. Ensure Redis is working via:

```sh
\>redis-cli ping
PONG <----what you should see
```

There are two Celery services: the main worker, which processes requests, and beat, which handles the scheduling of periodic tasks. They will each need to be started in separate terminals via:

`celery -A CYB_PHYS_CAPSTONE worker -l info`

and

`celery -A CYB_PHYS_CAPSTONE beat`
