from django.urls import path
from . import views

urlpatterns = [
    path("", views.MyfirstClass.as_view(), name='firstview')
]
