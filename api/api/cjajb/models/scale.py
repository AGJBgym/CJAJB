from django.db import models

class Scale(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=16, unique=True)
    