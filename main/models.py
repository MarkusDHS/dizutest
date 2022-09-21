from django.db import models

# Create your models here.

class Dl(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=1000)
    file=models.CharField(max_length=200)