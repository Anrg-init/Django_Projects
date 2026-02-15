from django.urls import path
from django.views.generic import TemplateView, RedirectView
from . import views
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('home/', RedirectView.as_view(url='/', permanent=False)),
    path('ghar/', RedirectView.as_view(pattern_name = 'home')),
    path('newhome/', views.newhome.as_view())
]

