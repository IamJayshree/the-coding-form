from django.db import models
from datetime import datetime

class Question(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField()          
    description = models.TextField(blank=True)
    is_Published = models.BooleanField(default = True)
    q_date = models.DateTimeField(default = datetime.now,blank = True)

    def __str__(self):
        return self.name
