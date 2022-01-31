from django.db import models

# Create your models here.


class StudentModel(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    school=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
   