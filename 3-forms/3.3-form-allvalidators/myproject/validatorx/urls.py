from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="formhomepage"),
    path("success/", views.success, name="successpage")
]
