from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from lunch_service.models import Restaurant, Dishes, Menus
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
    queryset = Menus.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return MenuReadSerializer
        return MenuSerializer
