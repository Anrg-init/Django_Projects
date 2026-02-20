from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField()
    age = models.IntegerField()
    city = models.CharField()
    desciption = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
