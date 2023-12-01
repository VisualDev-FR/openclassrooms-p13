from django.test import Client
import pytest


@pytest.mark.django_db
def test_profiles_index():
    """
    Test the global profiles view
    """
    client = Client()

    response = client.get("/profiles/")

    assert response.status_code == 200
    assert b"HeadlinesGazer" in response.content
    assert b"DavWin" in response.content
    assert b"AirWow" in response.content
    assert b"4meRomance" in response.content


@pytest.mark.django_db
def test_profile_single_view():
    """
    Test that single profile views are correctly displayed.
    """
    client = Client()

    # test profile 1
    response = client.get("/profiles/HeadlinesGazer/")

    assert response.status_code == 200
    assert b"<p><strong>First name :</strong> Jamie</p>" in response.content
    assert b"<p><strong>Last name :</strong> Lal</p>" in response.content

    # test profile 3
    response = client.get("/profiles/AirWow/")

    assert response.status_code == 200
    assert b"<p><strong>First name :</strong> Ada</p>" in response.content
    assert b"<p><strong>Last name :</strong> Paul</p>" in response.content
