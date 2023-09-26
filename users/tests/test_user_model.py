import pytest
from django.contrib.auth import get_user_model


Employee = get_user_model()


@pytest.fixture
def user_data():
    return {
        "email": "test@example.com",
        "password": "testpassword",
        "is_staff": False,
        "is_superuser": False,
    }

@pytest.fixture
def superuser_data():
    return {
        "email": "admin@example.com",
        "password": "adminpassword",
        "is_staff": True,
        "is_superuser": True,
    }

@pytest.fixture
def create_employee(user_data):
    return get_user_model().objects.create_user(**user_data)

@pytest.fixture
def create_superemployee(superuser_data):
    return get_user_model().objects.create_superuser(**superuser_data)


@pytest.mark.django_db
def test_create_employee(create_employee):
    employee = create_employee
    assert employee.email == "test@example.com"
    assert employee.is_staff is False
    assert employee.is_superuser is False
    assert employee.check_password("testpassword")

@pytest.mark.django_db
def test_create_superemployee(create_superemployee):
    superemployee = create_superemployee
    assert superemployee.email == "admin@example.com"
    assert superemployee.is_staff is True
    assert superemployee.is_superuser is True
    assert superemployee.check_password("adminpassword")


@pytest.mark.django_db
def test_create_employee_invalid_email():
    with pytest.raises(ValueError):
        Employee.objects.create_user(email="", password="testpassword")
