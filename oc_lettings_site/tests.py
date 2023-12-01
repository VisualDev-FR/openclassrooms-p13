from django.test import Client
from django.test.utils import override_settings
import pytest


@pytest.mark.django_db
def test_home_page():
    """
    Test the home page is available
    """
    client = Client()

    response = client.get("/")

    print(response.content)

    assert response.status_code == 200
    assert b'href="/profiles/"' in response.content
    assert b'href="/lettings/"' in response.content


@pytest.mark.django_db
def test_404_page():
    """
    Test that the custom 404 page is correctly displayed.
    """
    client = Client()

    response = client.get("/unexisting_page")

    assert response.status_code == 404
    assert b"<h1>404 - Page not found</h1>" in response.content
    assert b"<p>Sorry, the page you requested does not exist.</p>" in response.content


@override_settings(DEBUG=False)
@pytest.mark.django_db
def test_500_page():
    """
    Test that the custom 500 page is correctly displayed.
    """
    client = Client()

    with pytest.raises(Exception):
        response = client.get("/profiles/argument_crashing_the_app/")

        assert response.status_code == 500
        assert b"<h1>500 - Internal Error</h1>" in response.content
        assert b"<p>An error occured....</p>" in response.content
