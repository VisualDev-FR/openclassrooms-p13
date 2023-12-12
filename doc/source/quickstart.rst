Quickstart
====

.. _prerequisites:
Prerequisites
----

Accounts:

- `GitHub <https://github.com/>`_ account with read access to `this repository <https://github.com/VisualDev-FR/openclassrooms-p13>`_
- `Sentry.io <https://sentry.io/>`_ account, with a project configured for the oc_lettings app

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

    cd /path/to/cloned/repo

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

.. _run_django:
Run the site with Django
----
.. code:: bash

    cd /path/to/cloned/repo

.. code:: bash

    venv/bin/activate`

.. code:: bash

    pip install -r requirements.txt`

.. code:: bash

    python manage.py runserver 0.0.0.0:8000

- Go to http://localhost:8000 in a browser.
- Confirm that the site is working, and you can navigate (you should see several profiles and locations).

.. _run_docker:
Run the site with Docker
----

As an alternative to run the site with django, you can build and run a docker container.

.. code:: bash

    cd /path/to/cloned/repo

- Build the docker image
.. code:: bash

    docker build
    --no-cache
    --tag <your_image_name>
    --build-arg OC_LETTING_SENTRY_KEY="$OC_LETTING_SENTRY_KEY"
    --build-arg OC_LETTING_SK="$OC_LETTING_SK"
    .

- Run the builded image
.. code:: bash

    docker run -p 8000:8000 <your_image_name>

- Go to http://localhost:8000 in a browser.
- Confirm that the site is working, and you can navigate (you should see several profiles and locations).

Linting
----

.. code:: bash

    cd /path/to/cloned/repo

.. code:: bash

    source venv/bin/activate

.. code:: bash

    python -m flake8

Unit Tests
----

.. code:: bash

    cd /path/to/cloned/repo

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

- :ref:`run_django` or :ref:`run_docker`
- Go to http://localhost:8000/admin
- Log in with the user **admin**, password **Abc1234!**
