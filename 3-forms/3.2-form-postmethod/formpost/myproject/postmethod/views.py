from django.shortcuts import render
from . import forms
from django.shortcuts import redirect


def student(request):
     # f_value = request.POST
    # print(f_value['name'])
    # print(f_value['age'])
    # print(f_value['city'])
    # print(f_value['email'])
    
    if request.method == "POST":
        fm = forms.student_form(request.POST)

        if fm.is_valid():

            name = fm.cleaned_data['name']
            age = fm.cleaned_data['age']
            city = fm.cleaned_data['city']
            email = fm.cleaned_data['email']

            print(f"{name} {age} {city} {email}")

            return redirect("studentform")

    else:
        fm = forms.student_form()

    return render(request, "postmethod/index.html", {"s_form": fm})


def succexx(request):
    return render(request, "postmethod/success.html")
