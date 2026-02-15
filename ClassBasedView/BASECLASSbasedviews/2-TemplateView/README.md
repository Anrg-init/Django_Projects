# 📘 Django TemplateView — Complete A to Z Guide

---

## 1️⃣ What is TemplateView?

`TemplateView` is a generic Class-Based View (CBV) used to:

- Render an HTML template
- Without writing manual GET logic
- For static or lightly dynamic pages

It is the simplest generic CBV.

---

## 2️⃣ Import

```python
from django.views.generic import TemplateView
3️⃣ Basic Usage
views.py
python
Copy code
class HomeView(TemplateView):
    template_name = "home.html"
urls.py
python
Copy code
path("", HomeView.as_view(), name="home")
✔ Automatically handles GET
✔ Returns rendered template

4️⃣ Equivalent Function-Based View
TemplateView does the same as:

python
Copy code
from django.shortcuts import render

def home(request):
    return render(request, "home.html")
TemplateView = automatic CBV version.

5️⃣ Required Attribute
template_name (Mandatory)
python
Copy code
template_name = "file.html"
Without this → Django raises error.

6️⃣ How It Works Internally
Request →
URL resolver →
as_view() →
View instance created →
dispatch() →
get() →
get_context_data() →
Template rendered →
Response returned

7️⃣ Passing Data to Template (Context)
Override:

python
Copy code
get_context_data()
Example
python
Copy code
class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["name"] = "Anurag"
        context["age"] = 20

        return context
Template
html
Copy code
{{ name }} {{ age }}
8️⃣ Why Use super()?
Keeps default context provided by Django.

Without it, you may lose built-in data.

9️⃣ Access URL Parameters
urls.py
python
Copy code
path("user/<int:id>/", UserView.as_view())
views.py
python
Copy code
class UserView(TemplateView):
    template_name = "user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["user_id"] = kwargs["id"]
        return context
🔟 Access Query Parameters
URL:

bash
Copy code
/page/?name=anurag
View:

python
Copy code
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)

    context["name"] = self.request.GET.get("name")
    return context
1️⃣1️⃣ Using Model Data
python
Copy code
from .models import Student

class StudentPage(TemplateView):
    template_name = "students.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["students"] = Student.objects.all()
        return context
1️⃣2️⃣ extra_context (Shortcut)
For static data only:

python
Copy code
class AboutView(TemplateView):
    template_name = "about.html"
    extra_context = {"title": "About Page"}
1️⃣3️⃣ Handling POST Requests
TemplateView is GET-focused, but POST can be added.

python
Copy code
from django.http import HttpResponse

class ContactView(TemplateView):
    template_name = "contact.html"

    def post(self, request):
        name = request.POST.get("name")
        return HttpResponse(name)
1️⃣4️⃣ Async Support (Django 5)
You can use async methods:

python
Copy code
class AsyncHome(TemplateView):
    template_name = "home.html"

    async def get(self, request, *args, **kwargs):
        return await super().get(request, *args, **kwargs)
Use async only when needed.

1️⃣5️⃣ Important Methods You Can Override
get()
Customize GET behavior

get_context_data()
Add template variables (most common)

render_to_response()
Customize rendering process

1️⃣6️⃣ Method Flow
scss
Copy code
dispatch()
   ↓
get()
   ↓
get_context_data()
   ↓
render_to_response()
1️⃣7️⃣ When to Use TemplateView
Use when:

✔ Static pages (Home, About, Contact)
✔ Light dynamic data
✔ Dashboard pages
✔ No complex form logic
✔ No CRUD operations

1️⃣8️⃣ When NOT to Use TemplateView
Avoid when:

❌ Handling forms → Use FormView
❌ Listing database objects → Use ListView
❌ Single object detail → Use DetailView
❌ Create/Update/Delete → Use generic CRUD views

1️⃣9️⃣ TemplateView vs Base View
Base View
python
Copy code
class MyView(View):
    def get(self, request):
        return render(request, "home.html")
TemplateView
python
Copy code
class MyView(TemplateView):
    template_name = "home.html"
TemplateView = cleaner + less code.

2️⃣0️⃣ TemplateView vs ListView
Feature	TemplateView	ListView
Purpose	Any template	List of objects
Model required	❌	✔
Auto queryset	❌	✔

2️⃣1️⃣ Full Working Example
views.py
python
Copy code
from django.views.generic import TemplateView
from .models import Student

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["title"] = "Dashboard"
        context["students"] = Student.objects.all()

        return context
urls.py
python
Copy code
from django.urls import path
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
template (home.html)
html
Copy code
<h1>{{ title }}</h1>

{% for s in students %}
    {{ s.name }} — {{ s.age }} <br>
{% endfor %}
2️⃣2️⃣ Advantages
✔ Very simple to use
✔ Clean OOP structure
✔ Less boilerplate code
✔ Reusable via inheritance
✔ Built-in Django support

2️⃣3️⃣ Limitations
❌ Not designed for forms
❌ No automatic model handling
❌ No CRUD features
❌ Manual data fetching required

2️⃣4️⃣ Internal Architecture Summary
scss
Copy code
Client Request
     ↓
URL Resolver
     ↓
as_view()
     ↓
View Instance
     ↓
dispatch()
     ↓
get()
     ↓
get_context_data()
     ↓
Template Rendering
     ↓
HTTP Response
🚀 Final Summary
TemplateView is:

✔ The simplest generic CBV
✔ Used to render templates quickly
✔ Ideal for static or light dynamic pages
✔ Easy context handling
✔ Supports async in Django 5

It is usually the first generic CBV developers learn.

🧠 Recommended Learning Order (CBVs)
Base View

TemplateView

ListView

DetailView

FormView

Create/Update/Delete Views

Mastering TemplateView makes other generic views easier.

Copy code






