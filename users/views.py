from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSerializer


class ManageUserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

