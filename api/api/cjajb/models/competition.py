from django.db import models

class Competition(models.Model):
    discipline = models.ForeignKey('Discipline', on_delete=models.CASCADE, related_name='competitions')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='competitions')
    scale = models.ForeignKey('Scale', on_delete=models.CASCADE, related_name='competitions')
    competition = models.ForeignKey('Competition', on_delete=models.CASCADE, related_name='competitions', null=True)
    meeting = models.ForeignKey('Meeting', on_delete=models.CASCADE, related_name='competitions')
    
    