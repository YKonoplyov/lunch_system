from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    username = None
    email = models.EmailField("email address", unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

