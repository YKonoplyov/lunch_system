from django.db.models import Count, F
from django.utils import timezone
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from vote_service.models import Votes
from vote_service.permissions import HasNotVoted
from vote_service.serializers import VoteSerializer, VoteResultsSerializer


class VoteCreateView(CreateAPIView):
    serializer_class = VoteSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated, HasNotVoted]

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(employee=self.request.user)


class GetVoteResultsView(APIView):
    def get_serializer_class(self, request):
        if self.request.method == "GET":
            return VoteResultsSerializer

    def get_queryset(self):
        return Votes.objects.all()

    def get_vote_results(self):
        queryset = self.get_queryset()
        results = queryset.filter(
            date_voted=timezone.now().date()
        ).annotate(
            menu_name=F('menu__name')
        ).values("menu_name").annotate(
            votes_count=Count('menu_id')
        )
        return list(results)

    def get(self, request):
        results_data = self.get_vote_results()
        serializer_class = self.get_serializer_class(request=request)
        serializer = serializer_class(
            data=results_data,
            many=True
        )
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)
