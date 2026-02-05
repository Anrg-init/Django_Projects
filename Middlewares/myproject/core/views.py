from django.shortcuts import render

# Create your views here.
def home(request):
    print("i am home wala view")
    return render(request, "core/home.html")


def bio(request):
    print("this is bio page")
    return render(request, "core/bio.html")