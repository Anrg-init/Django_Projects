from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="homepage"),
    path("contact/", views.contact, name='contact'),
    path("about/", views.aboutus, name = 'about')
]
