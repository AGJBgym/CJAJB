from django.db import models

class Discipline(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=16, unique=True)
    callroom_time = models.TimeField()
    gathering_time = models.TimeField()
    
    
    