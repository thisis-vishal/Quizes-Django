from django.db import models
import datetime

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class QuizData(models.Model):
   question=models.CharField(max_length=500)
   options = models.JSONField()
   rightAnswer=models.IntegerField()
   startDate=models.DateTimeField()
   endDate=models.DateTimeField()
   status=models.CharField(max_length=10,null=True)