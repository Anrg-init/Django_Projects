from django.shortcuts import render
from asgiref.sync import sync_to_async
from . import models
from django.http import JsonResponse





# Create your views here.


# #sysnc function
# def my_sync_func(x):
#     return x * 2


# #async function

# async def my_async_func():
#     result = await sync_to_async(my_sync_func)(5)
#     print(result)



# #now changing from async to sync

# async def my_async_func2(x):
#     return x+21

# def my_sync_func2():
#     result = async_to_sync(my_async_func2)(9)
#     print(result)




# def get_student_data():
#     return list(models.Student.objects.filter(age=20).values())


async def student_data(request):
    data = await sync_to_async(
        lambda: list(models.Student.objects.filter(age=21).values())
    )()
    
    return JsonResponse({'data': data})

