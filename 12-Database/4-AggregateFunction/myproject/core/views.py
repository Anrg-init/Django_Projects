from django.shortcuts import render
from .models import Student
# from .models import Teacher

# check official dov of django for the querysets 


def home(request):

    # all_data = Student.objects.all()
    # all_data = Student.objects.create(..........all the fields are and it will directly send to the database)
    # all_data = Student.objects.get(pk=7)
    all_data = Student.objects.filter(name__contains ="i")
    print(all_data)

    return render(request, "core/home.html", {"students": all_data})



# Django ORM Aggregate Functions (One-File)

# Used to perform **calculations at database level**.

# # Import:

# # ```python
# from django.db.models import Count, Sum, Avg, Min, Max
# ```

# # ---

# ## Aggregate Functions

# * Count()  → count total rows
# * Sum()    → sum of values
# * Avg()    → average value
# * Min()    → minimum value
# * Max()    → maximum value

# ---

# ## Key Rule

# * `aggregate()` returns **ONE dictionary**
# * Not a QuerySet

# ---

# ## One Simple Example

# ### Model

# ```python
# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     marks = models.IntegerField()
# ```

# ### Query

# ```python
# result = Student.objects.aggregate(
#     total_students=Count('id'),
#     total_marks=Sum('marks'),
#     average_marks=Avg('marks'),
#     min_marks=Min('marks'),
#     max_marks=Max('marks')
# )

# print(result)
# ```

# ### Output

# ```python
# {
#   'total_students': 50,
#   'total_marks': 3625,
#   'average_marks': 72.5,
# ```
