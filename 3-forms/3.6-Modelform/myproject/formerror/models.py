from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=123)
    age = models.IntegerField(max_length=32)
    email = models.EmailField(max_length=123)