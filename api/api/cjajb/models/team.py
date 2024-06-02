from django.db import models

from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=16, unique=True)
    managers = models.ManyToManyField(User, related_name='teams')
    