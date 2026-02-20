from django.shortcuts import render
from .models import Student
from .models import Teacher

# check official dov of django for the querysets 


def home(request):
    # students = Student.objects.all()
    qs1 = Student.objects.values_list('id', 'name',named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)

    all_data = qs2.difference(qs1)


    return render(request, "core/home.html", {"students": all_data})







# Django ORM – most used & important queries

# Student.objects.all()                     # get all records
# Student.objects.filter(age=21)            # filter (WHERE)
# Student.objects.exclude(age=21)            # exclude (NOT)
# Student.objects.get(id=1)                 # get single record

# Student.objects.first()                   # first row
# Student.objects.last()                    # last row
# Student.objects.exists()                  # check existence
# Student.objects.count()                   # total count

# Student.objects.filter(age__gt=18)         # greater than
# Student.objects.filter(age__lt=30)         # less than
# Student.objects.filter(name__icontains="a")# case-insensitive search

# Student.objects.order_by('age')            # ascending order
# Student.objects.order_by('-age')           # descending order
# Student.objects.all()[:5]                  # limit results

# Student.objects.values()                   # dict-like output
# Student.objects.values_list('name','age')  # tuple output

# Student.objects.create(name="Rahul", age=21, teacher=t)  # insert
# Student.objects.filter(id=1).update(age=22)              # update
# Student.objects.filter(id=1).delete()                     # delete
