import datetime
from djongo import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class QuizData(models.Model):
   question=models.CharField(max_length=500)
   options = models.JSONField()
   rightAnswer=models.IntegerField()
   startDate=models.DateTimeField()
   endDate=models.DateTimeField()
   status=models.CharField(max_length=10,null=True)