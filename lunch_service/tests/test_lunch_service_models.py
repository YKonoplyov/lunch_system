import pytest
from django.db import IntegrityError
from django.utils import timezone
from lunch_service.models import Restaurant, Tags, Dishes, Menus

@pytest.fixture
def create_restaurant():
    return Restaurant.objects.create(
        name="Test Restaurant",
        description="A test restaurant for testing."
    )

@pytest.fixture
def create_tag():
    return Tags.objects.create(name="Test Tag")

@pytest.fixture
def create_dish():
    return Dishes.objects.create(
        name="Test Dish",
        ingredients="Ingredient 1, Ingredient 2"
    )

@pytest.fixture
def create_menu(create_dish, create_tag, create_restaurant):
    menu = Menus.objects.create(
        name="Test Menu",
        date=timezone.now(),
        restaurant=create_restaurant
    )
    menu.dishes.add(create_dish)
    menu.tags.add(create_tag)
    return menu

@pytest.mark.django_db
def test_create_restaurant(create_restaurant):
    restaurant = create_restaurant
    assert restaurant.name == "Test Restaurant"
    assert restaurant.description == "A test restaurant for testing."

@pytest.mark.django_db
def test_unique_name(create_restaurant):
    Restaurant.objects.create(name="Unique Restaurant", description="Description 1")
    with pytest.raises(IntegrityError):
        Restaurant.objects.create(name="Unique Restaurant", description="Description 2")

@pytest.mark.django_db
def test_create_tag(create_tag):
    tag = create_tag
    assert tag.name == "Test Tag"

@pytest.mark.django_db
def test_create_dish(create_dish):
    dish = create_dish
    assert dish.name == "Test Dish"
    assert dish.ingredients == "Ingredient 1, Ingredient 2"

@pytest.mark.django_db
def test_create_menu(create_menu, create_dish, create_tag):
    menu = create_menu
    dish = create_dish
    tag = create_tag
    assert menu.name == "Test Menu"
    assert menu.date.date() == timezone.now().date()
    assert dish in list(menu.dishes.all())
    assert tag in list(menu.tags.all())


@pytest.mark.django_db
def test_unique_name_date(create_restaurant):
    Menus.objects.create(name="Menu 1", date=timezone.now(), restaurant=create_restaurant)
    with pytest.raises(IntegrityError):
        Menus.objects.create(name="Menu 1", date=timezone.now(), restaurant=create_restaurant)