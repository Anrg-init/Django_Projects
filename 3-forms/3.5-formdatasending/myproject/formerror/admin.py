from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.profile)

class profileAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')