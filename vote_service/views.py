from django.db.models import Count, F, Q
from django.db.models.functions import Coalesce
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from lunch_service.models import Menus
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
        today = timezone.now().date()
        date_voted = self.request.query_params.get("date_voted")
        if date_voted:
            return Menus.objects.filter(date=date_voted)
        return Menus.objects.filter(date=today)

    def get_vote_results(self, filter_date: timezone = timezone.now().date()):
        queryset = self.get_queryset()
        vote_results = queryset.annotate(
            votes_count=Count(
                'votes', filter=Q(votes__date_voted=filter_date)
            )
        ).annotate(menu_name=F("name")).values('menu_name').annotate(
            votes_count=Coalesce('votes_count', 0)
        ).order_by("-votes_count")
        return list(vote_results)

    def get(self, request):
        date_voted = self.request.query_params.get("date_voted")

        results_data = self.get_vote_results()

        if date_voted:
            results_data = self.get_vote_results(date_voted)

        if not results_data:
            return Response({"message": "There is no vote "
                                        f"data for {date_voted}"})

        serializer_class = self.get_serializer_class(request=request)
        serializer = serializer_class(
            data=results_data,
            many=True
        )
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
