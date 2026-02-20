from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def signup(request):
    fm = forms.register()
    return render(request, "registration/signup.html", {'forms': fm})