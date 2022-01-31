from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPost(models.Model):
    who_post=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    comment=models.CharField(max_length=1000)