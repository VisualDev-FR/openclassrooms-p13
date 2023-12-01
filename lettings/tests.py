from django.test import Client
from django.urls import reverse, resolve
import pytest


@pytest.mark.django_db
def test_letting_urls():
    """
    Test that the name views and url are correct
    """

    # test index view
    path = reverse("lettings:index")

    assert path == "/lettings/"
    assert resolve(path).view_name == "lettings:index"

    # test single views
    path = reverse("lettings:letting", args=[1])

    assert path == "/lettings/1/"
    assert resolve(path).view_name == "lettings:letting"


@pytest.mark.django_db
def test_lettings_index():
    """
    Test the global lettings view
    """
    client = Client()

    response = client.get("/lettings/")

    assert response.status_code == 200
    assert b"Joshua Tree Green Haus /w Hot Tub" in response.content
    assert b"Oceanview Retreat" in response.content


@pytest.mark.django_db
def test_letting_single_view():
    """
    Test that single letting views are correctly displayed.
    """
    client = Client()

    # test letting 1
    response = client.get("/lettings/1/")

    assert response.status_code == 200
    assert b"Joshua Tree Green Haus /w Hot Tub" in response.content
    assert b"7217 Bedford Street" in response.content
    assert b"Brunswick, GA 31525" in response.content

    # test letting 3
    response = client.get("/lettings/3/")

    assert response.status_code == 200
    assert b"&#x27;Silo Studio&#x27; Cottage" in response.content
    assert b"340 Wintergreen Avenue" in response.content
    assert b"Newport News, VA 23601" in response.content
