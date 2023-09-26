from django.urls import path, include
from rest_framework import routers

from lunch_service.views import (
    RestaurantCreateView,
    TagCreateView,
    DishesViewSet,
    MenuViewSet,
)

lunch_service_router = routers.DefaultRouter()
lunch_service_router.register("dishes", DishesViewSet)
lunch_service_router.register("menus", MenuViewSet)

urlpatterns = [
    path("restaurants/", RestaurantCreateView.as_view(), name="restaurants"),
    path("tags/", TagCreateView.as_view(), name="tags"),
    path("", include(lunch_service_router.urls)),
]

app_name = "lunch-service"
