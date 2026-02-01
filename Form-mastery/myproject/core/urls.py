from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="homepage"),
    path('candidate/<int:pk>', views.Candidate_detail, name="candidate_detail_page")
]
