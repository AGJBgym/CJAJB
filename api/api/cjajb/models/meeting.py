from django.db import models

class Meeting(models.Model):
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    description = models.TextField()
    organizer = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='meetings')
    venue = models.ForeignKey('Venue', on_delete=models.CASCADE, related_name='meetings')
    championship = models.ForeignKey('Championship', on_delete=models.CASCADE, related_name='meetings')
    season = models.CharField(max_length=1, choices=[('O', 'Outdoor'), ('I', 'Indoor')])