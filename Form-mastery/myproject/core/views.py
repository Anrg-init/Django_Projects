from django.shortcuts import render
from . import forms
from django.shortcuts import redirect
from . import models
from django.contrib import messages

# Create your views here.
def home(request):
    Cand_list = models.Profile.objects.all()

    if request.method == 'POST':
        fm = forms.ProfileForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Profile Saved Succesfully")
            return redirect('homepage')
    else:
        fm = forms.ProfileForm()
            


    return render(request, "core/home.html", context={'form':fm, 'C_list': Cand_list})



def Candidate_detail(request, pk):
    Candidate = models.Profile.objects.get(pk = pk)
    return render(request, "core/candidate.html", {'Candidate_lst': Candidate})