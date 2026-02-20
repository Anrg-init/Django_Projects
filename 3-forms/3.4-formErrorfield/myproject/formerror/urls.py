from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="formhomepage"),
    path("successx/", views.successx, name="successpage")
]
