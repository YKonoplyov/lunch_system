from django.urls import path, include
from rest_framework import routers

from lunch_service.views import RestaurantCreateView, TagCreateView
    DishesViewSet,
lunch_service_router = routers.DefaultRouter()
lunch_service_router.register("dishes", DishesViewSet)

urlpatterns = [
    path("restaurants/", RestaurantCreateView.as_view(), name="restaurants"),
    path("tags/", TagCreateView.as_view(), name="tags"),
]

app_name = "lunch-service"
