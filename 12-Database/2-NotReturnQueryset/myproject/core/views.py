from django.shortcuts import render
from .models import Student
# from .models import Teacher

# check official dov of django for the querysets 


def home(request):

    # all_data = Student.objects.all()
    # all_data = Student.objects.create(..........all the fields are and it will directly send to the database)
    all_data = Student.objects.get(pk=7)
    print(all_data)

    return render(request, "core/home.html", {"students": all_data})



# ORM methods that do NOT return a QuerySet

# .get()              # returns ONE object
# .create()           # returns created object
# .first()            # returns ONE object or None
# .last()             # returns ONE object or None
# .get_or_create()    # returns (object, created_bool)
# .update_or_create() # returns (object, created_bool)

# .count()            # returns int
# .exists()           # returns bool

# .aggregate()        # returns dict
# .delete()

# .in_bulk()    # returns dict {id: object}
# .latest()
# .earliest()