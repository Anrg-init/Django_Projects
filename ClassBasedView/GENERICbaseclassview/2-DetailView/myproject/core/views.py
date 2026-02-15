from django.shortcuts import render
from django.views import View
from . import models

# Create your views here.
class SingleStudentView(View):
    def get(self, request, pk):
        stu = models.Student.objects.get(pk = pk)
        return render(request, 'core/single_student.html', {'student': stu})
    
    
    
    

