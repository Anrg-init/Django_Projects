from django import forms

class registration(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    email = forms.EmailField()



# types of validation, 1-jo ek ek krke krna hota h usko baad m dekhenge 2-jo ek baar m hojae 3-custome validators 4-inbuild validators

# 2-wala validators

# def clean(self):
#     cleaned_data = super().clean()
#     name_clean = cleaned_data.get('name')
#     email_clean = cleaned_data.get('email')

#     if name_clean and len(name_clean) < 10:
#         self.add_error('name, enter more character')

#     if email_clean and len(email_clean) < 10:
#         self.add_error('email, enter the correct email')

#     return cleaned_data

# 3 -wala built in validator -direct form me use hove h londe
from django import forms
from django.core import validators

class registration(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10),
                                       validators.MinLengthValidator(3)]
                                       )
    age = forms.IntegerField(validators=[validators.integer_validator])
    email = forms.EmailField(validators = [validators.EmailValidator])


# 4 - kudhs se bnanae walae validators
# wo def krke fir raise  b use hota  h jisme search on net
# from django.core.exceptions import ValidationError

# def name_validator(value):
#     if len(value) < 4:
#         raise ValidationError("Name must be at least 4 characters")


# fir ye krna 

# email = forms.EmailField(validators = [name_validators])