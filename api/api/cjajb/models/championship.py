from django.db import models

class Championship(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=255)
    allowed_missing = models.IntegerField()