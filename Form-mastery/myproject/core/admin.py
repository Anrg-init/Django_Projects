from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Profile)
list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file' ]