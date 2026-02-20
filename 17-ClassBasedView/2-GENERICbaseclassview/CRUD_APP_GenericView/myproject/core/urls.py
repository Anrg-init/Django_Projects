from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.StudentCreateView.as_view(), name='create' ),
    path('list/', views.StudentListView.as_view(), name='list' ),
    path('update/<int:pk>/edit/', views.UpdateListView.as_view(), name='update'),
       path('delete/<int:pk>/remove/', views.DeleteListView.as_view(), name='delete')

]
