from django.db import models
from datetime import datetime

class Module(models.Model):
    qcode = models.IntegerField()
    titlename = models.CharField(max_length=200)    
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_Published = models.BooleanField(default = True)
    mod_date = models.DateTimeField(default = datetime.now,blank = True)

    def __str__(self):
        return self.titlename
