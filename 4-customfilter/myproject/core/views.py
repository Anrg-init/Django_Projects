from django.shortcuts import render

# Create your views here.
def home(request):

    data = "The sky is blue and the sky looks calm because the sky reflects the calm blue water and the blue sky feels peaceful."

    return render(request, "core/home.html", context={'data': data} )