from django import forms

class student_form(forms.Form):
    name = forms.CharField()
    age  = forms.IntegerField()
    city = forms.CharField()
    email = forms.EmailField()



# now learning abou validation, form me properly kudh se validation lgana two tareek h 
# 1 - vhi lmba wala ek ek kre lagan
# 2 - thoda easy and ek baar me hojatha isko sikthe h

    def clean(self):
        cleaned_data = super().clean()
        name_value = cleaned_data.get('name')
        email_value = cleaned_data.get('email')

        if name_value and len(name_value) < 4:
            self.add_error('name', 'enter more than or equal to 4 character')

        if email_value and len(email_value) < 5:
            self.add_error('emal', 'enter correct email')

        return cleaned_data
        
        