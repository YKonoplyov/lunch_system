from django.urls import path

from lunch_service.views import RestaurantCreateView, TagCreateView
lunch_service_router = routers.DefaultRouter()

urlpatterns = [
    path("restaurants/", RestaurantCreateView.as_view(), name="restaurants"),
    path("tags/", TagCreateView.as_view(), name="tags"),
]

app_name = "lunch-service"
