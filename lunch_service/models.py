from django.db import models
from django.utils import timezone


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Dishes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField()

    def __str__(self):
        return self.name


class Menus(models.Model):
    name = models.CharField(max_length=255)
    dishes = models.ManyToManyField(Dishes, related_name="menus")
    tags = models.ManyToManyField(Tags, related_name="menus")
    date = models.DateField(default=timezone.now().date())
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "date"], name="name_date_unique"
            )
        ]

    def __str__(self):
        return self.name
