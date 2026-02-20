from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
        #.cascade ki jgah update delete or b bhot kuch add kr skthe  h
    )
    role = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
