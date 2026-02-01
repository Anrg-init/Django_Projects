from . import models
from django import forms
from .models import INDIAN_STATES

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

JOB_CITY_CHOICES = [
    ("", "Select job city"),
    ('DL', 'Delhi'),
    ('MB', 'Mumbai'),
    ('BL', 'Bangalore'),
    ('CH', 'Chennai'),
    ('HY', 'Hyderabad'),
    ('PN', 'Pune'),
]


class ProfileForm(forms.ModelForm):

    #overwriting the gender and states and job city attributes coming from model attribute
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect
    )

    state = forms.ChoiceField(
        choices=INDIAN_STATES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )


    job_city = forms.MultipleChoiceField(
        choices=JOB_CITY_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )



    class Meta:
        model = models.Profile
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file' ]

        labels = {'name':'Name',
                  'dob': 'DOB',
                   'locality': 'Location',
                    'pin': 'Pincode', 
                    'mobile':'Mobile number',
                      'my_file': 'File'
                }
        
        help_texts = {'profile_image': 'optional, upload any pofile pic', 'my_file': 'optional dost'}



        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Full Name'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','type': 'date', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter current location'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter previous city'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter valid pincode'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }





