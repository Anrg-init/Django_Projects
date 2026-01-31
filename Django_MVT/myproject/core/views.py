from django.shortcuts import render
from . import forms
from . import models
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "core/home.html")


def aboutus(request):
    return render(request, "core/about/about.html")


def contact(request):
    if request.method == 'POST':
        obj = models.user_detail.objects.all()
        fm = forms.profile(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'message sent succesfully')
            

    return render(request, "core/contact/contact.html")

