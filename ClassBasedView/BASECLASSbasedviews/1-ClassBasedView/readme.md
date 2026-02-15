# 📘 Class-Based View (Base `View`) in Django 5 — Complete A to Z Guide

---

# 1️⃣ What is a Class-Based View (CBV)?

In Django, views can be written in two ways:

- Function-Based Views (FBV)
- Class-Based Views (CBV)

CBV uses Python classes to handle requests instead of functions.

---

# 2️⃣ Base Class: `View`

The most basic CBV in Django is:

```python
from django.views import View


View is the parent class of almost all other class-based views.

It handles:

HTTP method routing (GET, POST, PUT, DELETE)

Request dispatching

3️⃣ Basic Structure
from django.views import View
from django.http import HttpResponse

class MyView(View):

    def get(self, request):
        return HttpResponse("GET request")

    def post(self, request):
        return HttpResponse("POST request")

4️⃣ URL Configuration

You must use .as_view():

from django.urls import path
from .views import MyView

urlpatterns = [
    path("test/", MyView.as_view(), name="test"),
]


Important:

You NEVER pass the class directly.

Always use .as_view().

5️⃣ What .as_view() Does

.as_view():

Converts class into callable view function

Instantiates the class per request

Connects request to dispatch()

Without it → Django cannot use the class.

6️⃣ Internal Flow

When request comes:

Django calls MyView.as_view()

It creates new instance of MyView

Calls dispatch()

dispatch() checks request method

Calls matching method (get(), post() etc.)

7️⃣ The dispatch() Method

dispatch() decides which method to call.

Simplified version:

def dispatch(self, request, *args, **kwargs):
    if request.method == "GET":
        return self.get(request)
    elif request.method == "POST":
        return self.post(request)


You can override it:

class MyView(View):

    def dispatch(self, request, *args, **kwargs):
        print("Before any method")
        response = super().dispatch(request, *args, **kwargs)
        print("After any method")
        return response


Useful for:

Logging

Permission checks

Custom behavior

8️⃣ Supported HTTP Methods

You can define:

get()

post()

put()

delete()

patch()

head()

options()

If method not defined → Django returns 405 Method Not Allowed.

9️⃣ Handling Forms (POST Example)
class ContactView(View):

    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Hello {name}")

🔟 Using Class Attributes

You can define class variables:

class MyView(View):
    greeting = "Hello"

    def get(self, request):
        return HttpResponse(self.greeting)


Each request creates new instance, so instance variables are safe.

1️⃣1️⃣ Async Class-Based Views (Django 5)

Django 5 supports async methods.

class AsyncView(View):

    async def get(self, request):
        return HttpResponse("Async GET")


If method is async → Django handles it via ASGI.

Important:

Use async only if needed

Use async ORM methods inside

1️⃣2️⃣ Accessing URL Parameters
path("user/<int:id>/", UserView.as_view())


View:

class UserView(View):

    def get(self, request, id):
        return HttpResponse(f"User ID: {id}")


URL parameters go into method arguments.

1️⃣3️⃣ Accessing Query Parameters

URL:

/test/?name=anurag


View:

def get(self, request):
    name = request.GET.get("name")

1️⃣4️⃣ Returning JSON
from django.http import JsonResponse

class APIView(View):

    def get(self, request):
        return JsonResponse({"status": "ok"})

1️⃣5️⃣ When to Use Base View

Use base View when:

You want full control

You don’t need generic features

You want manual handling of GET/POST

1️⃣6️⃣ When NOT to Use Base View

Don’t use base View if:

You are doing CRUD

You need automatic form handling

You need list/detail behavior

Instead use:

ListView

DetailView

CreateView

UpdateView

DeleteView

1️⃣7️⃣ Advantages of CBV

✔ Cleaner structure
✔ Reusable via inheritance
✔ Better for large apps
✔ Organized HTTP handling

1️⃣8️⃣ FBV vs CBV Comparison

FBV:

def my_view(request):
    if request.method == "GET":
        ...


CBV:

class MyView(View):
    def get(self, request):
        ...


CBV separates logic per method → cleaner.

1️⃣9️⃣ Common Mistakes

❌ Forgetting .as_view()

Wrong:

path("test/", MyView)


Correct:

path("test/", MyView.as_view())


❌ Mixing sync and async incorrectly

If using async method → run under ASGI.

2️⃣0️⃣ Complete Example

views.py:

from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class StudentView(View):

    def get(self, request):
        return HttpResponse("Student Page")

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(f"Received {name}")


urls.py:

from django.urls import path
from .views import StudentView

urlpatterns = [
    path("students/", StudentView.as_view(), name="students"),
]

2️⃣1️⃣ Internal Architecture Summary

Request →
URL resolver →
as_view() →
New View instance →
dispatch() →
get()/post() →
Response

2️⃣2️⃣ Final Summary

Base View in Django 5:

✔ Routes HTTP methods
✔ Uses dispatch() internally
✔ Requires .as_view()
✔ Supports async methods
✔ Gives full control

It is the foundation of all generic class-based views.

🚀 Learning Advice

First master:

FBV

Base View

dispatch()

Then generic CBVs

Understanding View makes all other CBVs easy.

j