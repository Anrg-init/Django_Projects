from django.shortcuts import render
from django.views.decorators.cache import cache_page

# Create your views here.
def home(request):
    return render(request, "core/home.html")


@cache_page(timeout=20)
def read(request):
    return render(request, "core/read.html")


def write(request):
    return render(request, "core/write.html")