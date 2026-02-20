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










# # Django ORM Field Lookups (One‑File Cheat Sheet)

# Use as:

# ```python
# Model.objects.filter(field__lookup=value)
# ```

# ---

# ## Basic / Exact

# * exact
# * iexact

# ## Contains / String Matching

# * contains
# * icontains
# * startswith
# * istartswith
# * endswith
# * iendswith

# ## Comparison

# * gt
# * gte
# * lt
# * lte

# ## Range / Set

# * in
# * range

# ## Null / Boolean

# * isnull

# ## Date & Time (DateField / DateTimeField)

# * date
# * year
# * month
# * day
# * week
# * week_day
# * quarter
# * time
# * hour
# * minute
# * second

# ## Regex

# * regex
# * iregex

# ## Relations (ForeignKey / OneToOne / ManyToMany)

# * exact (default)
# * in
# * double underscore traversal (author__name__icontains)

# ## JSONField (DB‑dependent)

# * contains
# * has_key
# * has_keys
# * has_any_keys

# ## Full‑Text Search (PostgreSQL)

# * search

# ---

# ## Example

# ```python
# Student.objects.filter(
#     name__icontains="anurag",
#     age__gte=18,
#     created_at__year=2025,
#     course__isnull=False
# )
# ```

# ---

# ✔ All common Django ORM field lookups in one place.
