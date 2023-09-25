from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()


class Tags(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Dishes(models.Model):
    name = models.CharField(max_length=255, unique=True)
    ingredients = models.TextField()
