import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

from lunch_service.models import Menus, Dishes, Tags, Restaurant


@pytest.fixture
def create_user():
    User = get_user_model()
    return User.objects.create_user(
        email="testuser@example.com",
        password="testpassword",
    )


@pytest.fixture
def api_client(create_user):
    user = create_user
    client = APIClient()
    client.force_authenticate(user=user)
    return client


@pytest.fixture
def create_menu(create_dish, create_tag):
    menu = Menus.objects.create(name="Test Menu")
    menu.dishes.add(create_dish)
    menu.tags.add(create_tag)
    return menu


@pytest.fixture
def create_restaurant():
    return Restaurant.objects.create(name="Test Restaurant", description="A test restaurant for testing.")


@pytest.fixture
def create_tag():
    return Tags.objects.create(name="Test Tag")


@pytest.fixture
def create_dish():
    return Dishes.objects.create(name="Test Dish", ingredients="Ingredient 1, Ingredient 2")


@pytest.mark.django_db
def test_create_restaurant(api_client):
    url = reverse("lunch-service:restaurants")
    data = {"name": "New Restaurant", "description": "A new restaurant for testing."}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_tag(api_client):
    url = reverse("lunch-service:tags")
    data = {"name": "New Tag"}
    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_dishes_viewset(api_client, create_dish):
    url = reverse("lunch-service:dishes-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_menu_viewset(api_client, create_menu):
    url = reverse("lunch-service:menus-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
