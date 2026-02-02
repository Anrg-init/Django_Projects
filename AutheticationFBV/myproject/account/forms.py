from django import forms 
from . import models

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget = forms.PasswordInput)
    class Meta:
        model = models.User

        fields = ['email', 'name', 'password', 'confirm_password']


        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                self.add_error('confirm password must match with password')

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if models.User.objects.filter(email = email).exists():
                raise forms.ValidationError("user with email already exist")





