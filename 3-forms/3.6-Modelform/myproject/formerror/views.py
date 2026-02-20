from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from . import models

# Create your views here.
# def home(request):
#     if request.method == 'POST':
#         form_value = forms.registration(request.POST)

#         if form_value.is_valid():
#             name_value = form_value.cleaned_data['name']
#             age_value = form_value.cleaned_data['age']
#             email_value = form_value.cleaned_data['email']

#             print(f""" {name_value} {age_value} {email_value} """)
#             return redirect("successpage")
        
#     fm = forms.registration()
#     return render(request, "formerror/home.html", {"forms":fm})


def home(request):
    if request.method == 'POST':
        fm = forms.registration(request.POST)

        if fm.is_valid():
            name_value = fm.cleaned_data['name']
            age_value = fm.cleaned_data['age']
            email_value = fm.cleaned_data['email']

            print(name_value, age_value, email_value)

            # saving coming data in database and printing too, just trying
            user = models.profile(name = name_value, age =age_value, email = email_value )
            user.save()
            return redirect("successpage")


            


    else:
        fm = forms.registration()

    return render(request, "formerror/home.html", {"forms": fm})



def successx(request):
    return render(request, "formerror/success.html")