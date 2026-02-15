from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
class MyfirstClass(View):
    def get(self, request):
        return HttpResponse("hey its working htklsdhfal ")