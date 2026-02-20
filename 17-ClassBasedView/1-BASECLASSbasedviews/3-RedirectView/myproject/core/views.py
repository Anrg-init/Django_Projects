from django.shortcuts import render
from django.views.generic.base import RedirectView

# Create your views here.

class newhome(RedirectView):
    url = 'https://www.google.com'
