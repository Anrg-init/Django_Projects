from django.urls import path, register_converter
from . import views
from .converters import FourDigitYearConverter

# register custom converter
register_converter(FourDigitYearConverter, 'year')

urlpatterns = [
    path('', views.home),

    path('user/<int:id>/', views.user_by_id),
    path('profile/<str:username>/', views.user_by_name),

    path('post/<slug:slug>/', views.post),

    # custom path converter
    path('archive/<year:yyyy>/', views.archive),
]
