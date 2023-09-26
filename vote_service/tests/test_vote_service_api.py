import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from lunch_service.models import Menus
from vote_service.models import Votes

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    return User.objects.create_user(
        email="testuser@example.com",
        password="testpassword",
    )


@pytest.fixture
def create_menu():
    return Menus.objects.create(name="Test Menu", date="2023-09-25")


@pytest.fixture
def create_vote(create_user, create_menu):
    return Votes.objects.create(
        employee=create_user,
        menu=create_menu,
        date_voted="2023-09-25",
    )


@pytest.mark.django_db
def test_create_vote(api_client, create_user):
    url = reverse("vote-service:make_vote")
    api_client.force_authenticate(user=create_user)
    response = api_client.post(url, data={"menu": 1})
    vote = Votes.objects.last()
    assert vote



@pytest.mark.django_db
def test_get_vote_results(api_client, create_vote):
    url = reverse("vote-service:voting_results")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
