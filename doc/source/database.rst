Database
====

Models overview
----

Three objects are represented in the database: Profile, Letting, Address.

- ``Profile`` : represents a client. It is linked to the Django ``User`` model (django.contrib.auth.models). Allows the identification of a user.

    .. autoclass:: profiles.models.Profile
        :members:
        :no-index:

- ``Letting``: represents a rental listing. Linked to an 'Address' to identify the object.

    .. autoclass:: lettings.models.Letting
        :members:
        :no-index:

- ``Address`` : represents a property for rent. The address of the property is provided.

    .. autoclass:: lettings.models.Address
        :members:
        :no-index:

Interact with the Database
----
.. code:: bash

    cd /path/to/cloned_repo

- Open a `sqlite3` shell session
- Connect to the database
.. code:: bash

    .open oc-lettings-site.sqlite3

- Display tables in the database
.. code:: bash

    .tables

- Display columns in the profiles table
.. code:: bash

    pragma table_info(Python-OC-Lettings-FR_profile);

- Execute a query on the profiles table
.. code:: bash

    select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

- ``.quit`` to exit