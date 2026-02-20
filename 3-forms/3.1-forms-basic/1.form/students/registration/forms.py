from django import forms

class register(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    city = forms.IntegerField()
    email = forms.EmailField()


