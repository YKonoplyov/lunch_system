from django.conf import settings
from django.db import models

from lunch_service.models import Menus
from users.models import Employee


class Votes(models.Model):
    employee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    menu = models.ForeignKey(
        Menus, on_delete=models.CASCADE, related_name="votes"
    )
    date_voted = models.DateField(auto_now_add=True)
