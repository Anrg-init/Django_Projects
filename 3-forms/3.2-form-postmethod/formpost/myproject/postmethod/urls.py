from . import views
from django.urls import path

urlpatterns = [
    path("student/", views.student, name="studentform"),
    path("success/", views.succexx, name='successform')
]
