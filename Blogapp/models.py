from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    content = models.CharField(max_length=250)
    image = models.ImageField()


    class Meta:
        db_table = "Myblog"
     
        