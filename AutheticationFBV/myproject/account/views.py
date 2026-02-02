from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.conf import settings
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from account.utils import send_activation_email
from . import models
from django.contrib.auth import logout


def home(request):
    return render(request, "account/home.html")


def aboutus(request):
    return render(request, "account/aboutus.html")


def register(request):
    if request.method == "POST":
        fm = forms.RegistrationForm(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)
            user.set_password(fm.cleaned_data["password"])
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            activation_link = reverse(
                'activate', kwargs={'uidb64': uidb64, 'token': token}
            )
            activation_url = f'{settings.SITE_DOMAIN}{activation_link}'

            send_activation_email(user.email, activation_url)

            messages.success(
                request,
                "registration successful, verify email to proceed"
            )
            return redirect('loginpage')
    else:
        fm = forms.RegistrationForm()

    return render(request, "account/register.html", {"form": fm})


def login(request):

    # If already logged in
    if request.user.is_authenticated:
        if request.user.is_seller:
            return redirect('seller_dashboard')
        elif request.user.is_customer:
            return redirect('customer_dashboard')
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Empty field check
        if not email or not password:
            messages.error(request, "Both fields are required.")
            return redirect('loginpage')

        try:
            user = models.User.objects.get(email=email)
        except models.User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('loginpage')

        # Password check
        if not user.check_password(password):
            messages.error(request, "Invalid email or password.")
            return redirect('loginpage')

        # Activation check
        if not user.is_active:
            messages.error(request, "Please activate your account first.")
            return redirect('loginpage')

        # Login user
        login(request, user)

        # Role based redirect
        if user.is_seller:
            return redirect('seller_dashboard')
        elif user.is_customer:
            return redirect('customer_dashboard')

        return redirect('home')

    return render(request, "account/login.html")








def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = models.User.objects.get(pk=uid)

        if user.is_active:
            messages.warning(request, "Account already activated")
            return redirect('loginpage')

        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(
                request,
                "Your account has been activated successfully"
            )
            return redirect("loginpage")
        else:
            messages.error(request, "The activation link is expired")
            return redirect('loginpage')

    except (TypeError, ValueError, OverflowError, models.User.DoesNotExist):
        messages.error(request, "Invalid activation link")
        return redirect('loginpage')


def sellerdashboard(request):
    return render(request, "account/sellerdashboard.html")


def customerdashboard(request):
    return render(request, "account/customerdashboard.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('loginpage')