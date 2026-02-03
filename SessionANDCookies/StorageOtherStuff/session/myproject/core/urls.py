from django.urls import path
from . import views

urlpatterns = [
    path('set/', views.setsession),
    path('get/', views.getsession),
    path('del/', views.delsession),
    path('flush/', views.flushsession),
    path('inview/', views.sessionmethodsinview),
    path('intemplate/', views.sessionmethodsintemplate),
    path('clear/', views.sessionclear),
    path('settest/', views.settestcookie),
    path('checktest/', views.checktestcookie),
    path('deltest/', views.deltestcookie),
]
