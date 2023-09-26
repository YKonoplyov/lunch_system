from django.utils import timezone
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet

from lunch_service.models import Dishes, Menus
from lunch_service.serializers import (
    RestaurantSerializer,
    TagsSerializer,
    DishSerializer,
    MenuReadSerializer,
    MenuSerializer,
)


class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantSerializer


class TagCreateView(CreateAPIView):
    serializer_class = TagsSerializer


class DishesViewSet(ModelViewSet):
    serializer_class = DishSerializer
    queryset = Dishes.objects.all()


class MenuViewSet(ModelViewSet):
    queryset = Menus.objects.filter(date=timezone.now().date())

    def get_serializer_class(self):
        if self.action == "create":
            return MenuSerializer
        if self.action == "update":
            return MenuSerializer
        return MenuReadSerializer
