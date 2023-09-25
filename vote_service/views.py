from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from vote_service.serializers import VoteSerializer
from vote_service.permissions import HasNotVoted


class VoteCreateView(CreateAPIView):
    serializer_class = VoteSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated, HasNotVoted]

    def perform_create(self, serializer):
        print(self.request)
        serializer.save(employee=self.request.user)
