from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
