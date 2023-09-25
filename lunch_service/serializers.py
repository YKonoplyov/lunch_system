from rest_framework.serializers import ModelSerializer

from lunch_service.models import Restaurant, Tags, Dishes


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