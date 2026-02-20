from . import models
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class StudentCreateView(CreateView):
    model = models.Student
    fields = ['name', 'age', 'city']
    success_url = '/student/'


class StudentListView(ListView):
    model = models.Student


class UpdateListView(UpdateView):
    model = models.Student
    fields = ['name', 'age']


class DeleteListView(DeleteView):
    model = models.Student
    success_url = reverse_lazy('list')

