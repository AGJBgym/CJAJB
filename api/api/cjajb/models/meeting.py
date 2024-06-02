from django.db import models

class Meeting(models.Model):
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='meetings')
    championship = models.ForeignKey('Championship', on_delete=models.CASCADE, related_name='meetings')