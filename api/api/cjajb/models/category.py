from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.IntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    