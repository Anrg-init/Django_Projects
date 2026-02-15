from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.SingleStudentView.as_view(), name='single_student')
]
