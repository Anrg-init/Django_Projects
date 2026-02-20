from django import forms
from . import models

# class registration(forms.Form):
#     name = forms.CharField(error_messages = {'required': 'enter correct naam'})
#     age = forms.IntegerField(error_messages = {'required': 'enter correct age'})
#     email = forms.EmailField() 

class registration(forms.ModelForm):
    # we can also overwrite the 
    password = forms.IntegerField(max_value = 123, required=True)


    class Meta:
        model = models.profile
        fields = ['name', 'age', 'email', 'password']
        labels = {'name': 'enter name', 'age':'enter real age', 'email': 'enter email'}
        error_messages = {'email': {'required': 'email is compulsory'}}
        widget = {'age': forms.PasswordInput()}


# we can also do form inheritance, jase ye registration  - ek new class ie form bnaeye fir usme isko registration ko inclde krlenge fr baaki ka same kaam h 

