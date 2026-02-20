from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

async def home(request):
    return HttpResponse("hey how are you")


    