from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from lunch_service.models import Restaurant
from lunch_service.serializers import RestaurantSerializer, TagsSerializer


class RestaurantCreateView(CreateAPIView):
    serializer_class = RestaurantSerializer


class TagCreateView(CreateAPIView):
    serializer_class = TagsSerializer