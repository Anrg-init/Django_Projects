from . import models
from django import forms

class profile(forms.ModelForm):
    class Meta:
        model = models.user_detail
        fields = ['name', 'email','message']


    