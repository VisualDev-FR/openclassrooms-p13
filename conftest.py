from django.conf import settings
import pytest


@pytest.fixture(scope="session")
def django_db_setup():
    """
    Fixture allowing to duplicate the given database for testing
    """
    settings.DATABASES["default"] = {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "oc-lettings-site.sqlite3",
    }
