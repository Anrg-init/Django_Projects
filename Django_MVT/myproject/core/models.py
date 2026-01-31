from django.db import models

# Create your models here.
class user_detail(models.Model):
    name = models.CharField(max_length=123)
    email = models.EmailField(max_length=311)
    message = models.TextField()