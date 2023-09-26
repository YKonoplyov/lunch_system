from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_data():
    return {
        "email": "test@example.com",
        "password": "testpassword",
    }


@pytest.mark.django_db
def test_create_user(api_client, user_data):
    url = reverse("users:create")
    response = api_client.post(url, user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["email"] == user_data["email"]
    assert response.data["is_staff"] is False
    assert len(get_user_model().objects.all()) == 1


@pytest.mark.django_db
def test_manage_user(api_client, user_data):
    admin = get_user_model().objects.create_superuser(**user_data)
    client = api_client

    client.force_authenticate(admin)

    url = reverse("users:manage-user")
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK

    response = client.patch(url, data={"email": "secondemail@mail.com"})

    assert response.status_code == status.HTTP_200_OK

    admin = get_user_model().objects.get(email="secondemail@mail.com")

    assert admin != None
