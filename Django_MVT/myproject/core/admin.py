from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.user_detail)

class userdetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')