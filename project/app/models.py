from django.db import models


class teacherTimeSheet (models.Model):
    teacher_Name = models.CharField(max_length=100)
    school_Name = models.CharField(max_length=100)
    subject_Name = models.CharField(max_length=100)
    hours = models.CharField(max_length=7)
    date_Of_Work = models.DateTimeField('date worked')
    date_Of_Entry = models.DateTimeField('date entered')


def __str__(self):
    return self.teacher_Name

