## Project overview

This project encompasses a straightforward web application designed to showcase user profiles and real estate listings. Users can conveniently view and interact with these components through the application’s user interface. Additionally, the system supports data editing functionalities accessible via the site’s administrative interface.

Full documentation of the project is available [here](https://openclassrooms-p13.readthedocs.io/en/latest/index.html)

## Local developement

### Prerequisites

Accounts:
- GitHub account with read access to this repository
- Sentry.io account, with a project configured for the oc_lettings app

Softwares:
- Git CLI
- Python interpreter, version 3.6 or higher
- Docker Desktop

Environement variables:
- OC_LETTING_SK = the secret key of the project
- OC_LETTING_SENTRY_KEY = your sentry DSN Key
- DJANGO_DEBUG = 0 or 1, to configure django on production mode

### Create virtual env

``cd /path/to/cloned/repo``

``python -m venv venv``

Activate the environment ``./venv/bin/activate``

To deactivate the environment ``deactivate``


### Run the site

- `cd /path/to/cloned/repo`
- `source venv/bin/activate`
- `pip install --requirement requirements-dev.txt`
- `python manage.py runserver 0.0.0.0:8000`

Go to http://localhost:8000 in a browser, and then confirm that the site is working, and you can navigate (you should see several profiles and locations).

### Linting

- `cd /path/to/cloned/repo`
- `source venv/bin/activate`
- `python -m flake8`

### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

### Test Coverage

``pytest --cov-config=setup.cfg --cov=. --cov-fail-under=80``

### Database

- `cd /path/to/cloned/repo`
- Open an `sqlite3` shell session
- Connect to the database `.open oc-lettings-site.sqlite3`
- Display database tables `.tables`
- Show columns in profile table `pragma table_info(Python-OC-Lettings-FR_profile);`
- Run a query on the profile table `select user_id, favorite_city from Python-OC-Lettings-FR_profile;`
- `.quit` to exit
