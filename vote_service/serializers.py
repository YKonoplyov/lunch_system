from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from vote_service.models import Votes
from lunch_service.models import Menus


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Votes
        exclude = ("date_voted", "employee")
        extra_kwargs = {
            "menu": {
                "queryset": Menus.objects.filter(date=timezone.now().date())
            }
        }


class VoteResultsSerializer(Serializer):
    menu_name = serializers.CharField(max_length=255)
    votes_count = serializers.IntegerField()
