from django.db import models

from cjajb.models.team import Team
from cjajb.models.category import Category

class Athlete(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])    
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='athletes')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='athletes')