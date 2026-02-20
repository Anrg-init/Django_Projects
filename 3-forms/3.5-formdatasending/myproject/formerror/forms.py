from django import forms

class registration(forms.Form):
    name = forms.CharField(error_messages = {'required': 'enter correct naam'})
    age = forms.IntegerField(error_messages = {'required': 'enter correct age'})
    email = forms.EmailField() 




# yrr gnd ftt gyi dekhlio baad me error field hacnding django kase krna h