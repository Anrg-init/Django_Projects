from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('user/', views.show_user_data, name='user_data'),
    path('page/', views.show_page_data, name='user_page'),
    path('post/', views.show_post_data, name='user_post'),
    path('song/', views.show_song_data, name='user_song'),

]
