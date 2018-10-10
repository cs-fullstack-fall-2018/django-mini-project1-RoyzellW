from django.db import models
from datetime import datetime

class TimeSheet(models.Model):
    Name_Of_Person = models.CharField(max_length=200)
    Name_Of_School = models.CharField(max_length=200)
    Name_Of_Subject = models.CharField(max_length=200)
    Date_of_Work = models.DateTimeField('date completed', default=datetime.now, blank=True)
    Date = models.DateTimeField(default=datetime.now, blank=True)




