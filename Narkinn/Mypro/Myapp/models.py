from django.db import models

# Create your models here.

class Managment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    text = models.TextField(max_length=1000)
    phone = models.TextField(max_length=100)
