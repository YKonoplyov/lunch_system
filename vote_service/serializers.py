from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from vote_service.models import Votes


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Votes
        exclude = ("date_voted", "employee")


class VoteResultsSerializer(Serializer):
    menu_name = serializers.CharField(max_length=255)
    votes_count = serializers.IntegerField()
