from django.db import models

# Create your models here.

class user(models.Model):
    telephone = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=64)
    name=models.CharField(max_length=20)