# from django.shortcuts import render
# from asgiref.sync import sync_to_async
from . import models
from django.http import HttpResponse



async def home(request):

    # async for student in models.Student.objects.all():
    #     print(f"{student.name} + {student.city} ")

    await models.Student.objects.acreate(
        name = "levan",
        age = 22,
        city = "nyc",
        description = "hksdfk"
    )

    return HttpResponse("workhhling")
