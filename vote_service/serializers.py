from rest_framework.serializers import ModelSerializer

from vote_service.models import Votes


class VoteSerializer(ModelSerializer):
    class Meta:
        model = Votes
        exclude = ("date_voted", "employee")