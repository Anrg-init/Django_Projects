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






# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.db.models import Q
# from .models import Profile, Issue


# def q_objects_examples(request):
#     """
#     Demonstrates all common Q object database operations
#     """

#     # 1. OR condition
#     users_or = User.objects.filter(
#         Q(username='admin') | Q(email='admin@gmail.com')
#     )

#     # 2. AND condition
#     users_and = User.objects.filter(
#         Q(is_active=True) & Q(is_staff=True)
#     )

#     # 3. NOT condition
#     non_admins = User.objects.filter(
#         ~Q(is_superuser=True)
#     )

#     # 4. AND + OR mixed
#     mixed_query = Profile.objects.filter(
#         Q(role='student') | Q(role='teacher'),
#         is_verified=True
#     )

#     # 5. Grouped / nested conditions
#     age_group = Profile.objects.filter(
#         (Q(age__gte=18) & Q(age__lte=25)) |
#         Q(role='teacher')
#     )

#     # 6. Dynamic Q building
#     q = Q()
#     role = request.GET.get('role')
#     min_age = request.GET.get('min_age')

#     if role:
#         q &= Q(role=role)

#     if min_age:
#         q &= Q(age__gte=min_age)

#     dynamic_profiles = Profile.objects.filter(q)

#     # 7. Q with field lookups
#     lookup_query = Profile.objects.filter(
#         Q(user__username__icontains='john') |
#         Q(role__startswith='stud')
#     )

#     # 8. Multiple Q objects
#     multi_q = Profile.objects.filter(
#         Q(role='student') |
#         Q(is_verified=True) |
#         Q(age__gt=30)
#     )

#     # 9. Q with exclude
#     excluded = Profile.objects.exclude(
#         Q(role='admin') | Q(is_verified=False)
#     )

#     # 10. Q with related models
#     issues = Issue.objects.filter(
#         Q(created_by__profile__role='teacher') |
#         Q(is_resolved=False)
#     )

#     # 11. Empty Q (returns all rows)
#     all_profiles = Profile.objects.filter(Q())

#     return render(request, "q_demo.html", {
#         "users_or": users_or,
#         "users_and": users_and,
#         "non_admins": non_admins,
#         "mixed_query": mixed_query,
#         "age_group": age_group,
#         "dynamic_profiles": dynamic_profiles,
#         "lookup_query": lookup_query,
#         "multi_q": multi_q,
#         "excluded": excluded,
#         "issues": issues,
#         "all_profiles": all_profiles,
#     })
