# Django 5 — DetailView (Generic Class-Based View) — A to Z Guide

## 📌 What is DetailView?

**DetailView** displays **ONE single object (record)** from the database.

👉 Example:  
- One book page  
- One product page  
- One blog post page  
- One user profile page  

If ListView = "list of items"  
Then DetailView = "single item page"

---

## 🧠 Real Website Examples

| Website | Detail Page |
|----------|------------|
Amazon | Single product page |
Flipkart | Product details page |
Blog site | Single post page |
YouTube | Video page |

---

## 📦 Import

```python
from django.views.generic import DetailView
🏗️ Basic Setup (Step-by-Step)
1️⃣ Model
python
Copy code
# models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.title
2️⃣ View
python
Copy code
# views.py

from django.views.generic import DetailView
from .models import Book

class BookDetailView(DetailView):
    model = Book
👉 That’s it. Django handles everything.

3️⃣ URL
DetailView needs object ID or slug

python
Copy code
# urls.py

from django.urls import path
from .views import BookDetailView

urlpatterns = [
    path("book/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
]
4️⃣ Template
Default template name:

Copy code
book_detail.html
👉 Format:

php-template
Copy code
<modelname>_detail.html
🧾 Default Template Context
Inside template you get:

Main object
csharp
Copy code
object
Example:

html
Copy code
<h1>{{ object.title }}</h1>
<p>Author: {{ object.author }}</p>
<p>Price: {{ object.price }}</p>
Also available:
nginx
Copy code
book
Django automatically adds model name in lowercase.

html
Copy code
<h1>{{ book.title }}</h1>
🔑 How DetailView Gets the Object
Internally:

python
Copy code
Book.objects.get(pk=pk_from_url)
So this URL:

bash
Copy code
/book/5/
Loads:

csharp
Copy code
Book.objects.get(pk=5)
⚙️ Important Attributes (A to Z)
✅ model
python
Copy code
model = Book
Auto fetches object.

✅ queryset (optional alternative)
Use this instead of model:

python
Copy code
queryset = Book.objects.filter(published=True)
✅ template_name
Change template file name:

python
Copy code
template_name = "books/single_book.html"
✅ context_object_name
Rename object variable in template:

python
Copy code
context_object_name = "mybook"
Template:

html
Copy code
{{ mybook.title }}
✅ pk_url_kwarg
Change URL parameter name for ID.

Default = pk

python
Copy code
pk_url_kwarg = "id"
URL:

python
Copy code
path("book/<int:id>/", BookDetailView.as_view())
✅ slug_field + slug_url_kwarg
Use slug instead of ID.

Model:
python
Copy code
slug = models.SlugField(unique=True)
View:
python
Copy code
slug_field = "slug"
slug_url_kwarg = "slug"
URL:
python
Copy code
path("book/<slug:slug>/", BookDetailView.as_view())
🧪 Custom Query — get_queryset()
Filter which objects can be accessed.

python
Copy code
def get_queryset(self):
    return Book.objects.filter(price__gt=100)
🎯 Access URL Data — self.kwargs
python
Copy code
def get_queryset(self):
    category = self.kwargs.get("category")
    return Book.objects.filter(category=category)
🧩 Add Extra Data — get_context_data()
Add additional variables to template.

python
Copy code
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["message"] = "Hello from DetailView"
    return context
Template:

html
Copy code
<p>{{ message }}</p>
🔄 Full Example (Professional Setup)
models.py
python
Copy code
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    slug = models.SlugField(unique=True)
views.py
python
Copy code
class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_page.html"
    context_object_name = "book"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_books"] = Book.objects.exclude(
            id=self.object.id
        )[:3]
        return context
urls.py
python
Copy code
path("book/<slug:slug>/", BookDetailView.as_view(), name="book_detail")
template
html
Copy code
<h1>{{ book.title }}</h1>
<p>{{ book.author }}</p>
<p>{{ book.price }}</p>

<h3>Related Books</h3>

{% for b in related_books %}
    <p>{{ b.title }}</p>
{% endfor %}
⚡ How Request Flow Works
User visits:

bash
Copy code
/book/5/
URL sends pk=5 to DetailView

DetailView fetches object

Sends object to template

Template renders page

❌ Common Mistakes
❌ No ID in URL
DetailView MUST know which object to show.

❌ Wrong template name
Default is:

php-template
Copy code
<modelname>_detail.html
❌ Object not found
Raises:

mathematica
Copy code
404 Not Found
🧠 When to Use DetailView?
Use when you need:

✔️ Single object page
✔️ Read-only display
✔️ Simple implementation
✔️ Clean code

🆚 DetailView vs ListView
Feature	ListView	DetailView
Objects	Many	One
Query	.all()	.get()
Use case	Product list	Product page

🚀 Advanced Use Cases
Product page

Blog post page

Profile page

Article page

Course detail page

Issue tracker item page

🏁 Final Summary
👉 DetailView = Display one database record
👉 Requires pk or slug in URL
👉 Auto fetches object
👉 Auto passes object to template
👉 Easily customizable

📌 One-Line Definition
DetailView is a Django generic class-based view used to display a single object from the database.

🔥 If you want next:

UpdateView A-Z

DeleteView A-Z

CreateView A-Z

Full CRUD with Class-Based Views

CBV vs FBV deep comparison

Just say 👍

Copy code
