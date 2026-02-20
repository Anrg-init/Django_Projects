# from django.shortcuts import render
# from . import forms
# from django.shortcuts import redirect

# def home(request):
#     if request.method == 'POST':
#         form_post = forms.registration(request.POST)

#         if form_post.is_valid():
#             name_final = form_post.cleaned_data['name']
#             age_final = form_post.cleaned_data['age']
#             email_final = form_post.cleaned_data['email']

#             print(name_final, age_final, email_final)

#             # show empty form again (or redirect)
#             fm = forms.registration()
#             return redirect("successpage")

#     else:
#         fm = forms.registration()
#         return render(request, "validatorx/index.html", {"forms": fm})


# def success(request):
#     return render(request, "validatorx/register.html")


from django.shortcuts import render, redirect
from . import forms

def home(request):
    if request.method == 'POST':
        form_post = forms.registration(request.POST)

        if form_post.is_valid():
            print(
                form_post.cleaned_data['name'],
                form_post.cleaned_data['age'],
                form_post.cleaned_data['email']
            )

            return redirect("successpage")

        # ❗ form invalid → return with errors
        return render(
            request,
            "validatorx/index.html",
            {"forms": form_post}
        )

    # GET request
    fm = forms.registration()
    return render(request, "validatorx/index.html", {"forms": fm})


def success(request):
    return render(request, "validatorx/register.html")
