from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from lunch_service.models import Restaurant, Tags, Dishes, Menus


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class DishSerializer(ModelSerializer):
    class Meta:
        model = Dishes
        fields = "__all__"


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menus
        fields = "__all__"


class MenuReadSerializer(MenuSerializer):
    tags = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True,
    )
    dishes = serializers.SlugRelatedField(
        slug_field="name", read_only=True, many=True,
    )
