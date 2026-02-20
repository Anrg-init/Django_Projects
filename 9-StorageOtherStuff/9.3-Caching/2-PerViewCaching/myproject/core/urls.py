from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path("home/", views.home ),
    path("write/", cache_page(20)(views.write)),
    path("read/", views.read )


]
