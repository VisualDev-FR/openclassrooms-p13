Installation
====

Prerequisites
----

Accounts:

- `GitHub <https://github.com/>`_ account with read access to `this repository <https://github.com/VisualDev-FR/openclassrooms-p13>`_
- `Sentry.io" <https://sentry.io/>`_ account, with a project configured for the oc_lettings app

Softwares:

- `Git CLI <https://git-scm.com/downloads>`_
- `Python interpreter <https://www.python.org/downloads/>`_, version 3.6 or higher
- `Docker Desktop <https://www.docker.com/products/docker-desktop/>`_

Environement variables:

- ``OC_LETTING_SK`` = the secret key of the project
- ``OC_LETTING_SENTRY_KEY`` = your sentry DSN Key
- ``DJANGO_DEBUG`` = 0 or 1, to configure django on production mode

Throughout the rest of the documentation for local development, it is assumed that the ``python`` command
in your OS shell executes the above Python interpreter (unless a virtual environment is activated).

Clone the Repository
----
.. code:: bash

    cd /path/to/put/project/in

.. code:: bash

    git clone https://github.com/VisualDev-FR/openclassrooms-p13

Create the Virtual Environment
----
- Create a new virtual env
.. code:: bash

    cd /path/to/Python-OC-Lettings-FR

.. code:: bash

    python -m venv venv

- Activate the environment
.. code:: bash

    ./venv/bin/activate

- upgrade pip
.. code:: bash

    pip install --upgrade pip

- To deactivate the environment
.. code:: bash

    deactivate

.. _run_site:
Run the site
----
.. code:: bash

    cd /path/to/Python-OC-Lettings-FR`

.. code:: bash

    venv/bin/activate`

.. code:: bash

    pip install -r requirements.txt`

.. code:: bash

    python manage.py runserver 0.0.0.0:8000

- Go to `http://localhost:8000` in a browser.
- Confirm that the site is working, and you can navigate (you should see several profiles and locations).

Linting
----

.. code:: bash

    cd /path/to/Python-OC-Lettings-FR

.. code:: bash

    source venv/bin/activate

.. code:: bash

    python -m flake8

Unit Tests
----

.. code:: bash

    cd /path/to/Python-OC-Lettings-FR

.. code:: bash

    source venv/bin/activate

.. code:: bash

    python -m pytest

Test Coverage
----

.. code:: bash

    pytest --cov-config=setup.cfg --cov=. --cov-report html


Administration Panel
----

- :ref:`run_site`
- Go to http://localhost:8000/admin
- Log in with the user **admin**, password **Abc1234!**