import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from vote_service.models import Votes
from lunch_service.tests.test_lunch_service_models import (
    create_menu,
    create_dish,
    create_tag,
    create_restaurant,
)

Employee = get_user_model()


@pytest.fixture
def create_employee():
    return Employee.objects.create_user(
        email="testuser@example.com",
        password="testpassword",
    )


@pytest.fixture
def create_vote(create_employee, create_menu):
    return Votes.objects.create(
        employee=create_employee,
        menu=create_menu,
    )


@pytest.mark.django_db
def test_create_vote(create_vote):
    vote = create_vote
    assert vote.employee.email == "testuser@example.com"
    assert vote.menu.name == "Test Menu"
    assert vote.date_voted == timezone.now().date()
