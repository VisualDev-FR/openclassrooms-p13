from django.test import Client
import pytest


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
