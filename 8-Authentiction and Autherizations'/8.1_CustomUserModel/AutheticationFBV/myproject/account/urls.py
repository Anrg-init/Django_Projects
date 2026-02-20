from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="homepage"),
    path("aboutus/", views.aboutus, name="aboutuspage"),
    path("register/", views.register, name="registerpage"),
    path("login/", views.login, name="loginpage"),
    path("activate/<str:uidb64>/<str:token>/", views.activate_account, name="activate"),
    path("sellerdashboard/", views.sellerdashboard, name="seller_dashboard"),
    path("customerdashboard/", views.customerdashboard, name="customer_dashboard"),
    path("logout/", views.logout_view, name="logout"),
]
