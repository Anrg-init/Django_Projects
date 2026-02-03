from django.urls import path
from . import views

urlpatterns = [
    path("getcookie/", views.getcookie, name="getcookie"),
    path("setcookie/", views.setcookie, name="setcookie"),
    path("delcookie/", views.delcookie, name="delcookie"),
    path("getscookie/", views.getsignedcookie, name="fuck"),
    path("setscookie/", views.setsignedcookie, name="you")

]
