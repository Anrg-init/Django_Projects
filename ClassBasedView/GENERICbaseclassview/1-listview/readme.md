# 📘 Django 5 — Generic Class-Based View: ListView (Complete Notes)

## 🔰 What is ListView?

**ListView** is a built-in Generic Class-Based View that displays a list of objects from a database model.

👉 Used for pages like:

* Product list
* Blog posts list
* Book catalog
* Users list
* Orders dashboard

---

## ⭐ Why use ListView instead of manual views?

Without ListView (manual TemplateView/View):

* You write DB queries yourself
* Pass context manually
* Handle pagination manually
* More code, more bugs

With ListView:

✅ Automatic queryset
✅ Automatic context variable
✅ Built-in pagination
✅ Cleaner & DRY code
✅ Industry standard

---

## 🧠 Basic Working Flow

```
Request → ListView → Fetch objects → Send to template → Render list
```

---

## 🧩 Minimal Example

### models.py

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title
```

---

### views.py

```python
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
```

---

### urls.py

```python
path('', BookListView.as_view(), name='book-list')
```

---

### Default Template Name

Django expects:

```
<app>/<model>_list.html
```

Example:

```
core/book_list.html
```

---

### Template Example

```html
<h2>Books</h2>

<ul>
{% for book in object_list %}
    <li>{{ book.title }} — {{ book.author }}</li>
{% empty %}
    <li>No books available</li>
{% endfor %}
</ul>
```

---

## ⭐ Important Default Attributes

### 1️⃣ model

Specifies which model to fetch.

```python
model = Book
```

---

### 2️⃣ queryset (optional)

Override default objects.

```python
queryset = Book.objects.filter(author="Arjun")
```

---

### 3️⃣ template_name

Custom template path.

```python
template_name = "core/my_books.html"
```

---

### 4️⃣ context_object_name

Rename `object_list`.

```python
context_object_name = "books"
```

Now template uses:

```django
{% for book in books %}
```

---

## 🧠 Default Context Variables

ListView sends:

| Variable        | Meaning         |
| --------------- | --------------- |
| object_list     | list of objects |
| model_name_list | e.g. book_list  |

---

## ⭐ Using get_queryset() (MOST IMPORTANT 🔥)

Override to apply dynamic logic.

```python
class BookListView(ListView):
    model = Book
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.filter(genre="thriller")
```

---

## ⭐ Filtering Using URL Parameters

Example:

```
/?genre=thriller
```

```python
def get_queryset(self):
    genre = self.request.GET.get("genre")
    qs = Book.objects.all()

    if genre:
        qs = qs.filter(genre=genre)

    return qs
```

---

## ⭐ Adding Extra Context Data

Use `get_context_data()`.

```python
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["title"] = "All Books"
    return context
```

---

## ⭐ Pagination (Built-in 🚀)

### views.py

```python
class BookListView(ListView):
    model = Book
    paginate_by = 5
```

---

### Template Pagination

```html
<div>
{% if is_paginated %}

    {% if page_obj.has_previous %}
        <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
    {% endif %}

    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}">Next</a>
    {% endif %}

{% endif %}
</div>
```

---

## ⭐ Ordering Results

### Static ordering

```python
ordering = ['-created_at']
```

---

### Dynamic ordering

```python
def get_queryset(self):
    return Book.objects.order_by('-created_at')
```

---

## ⭐ Combining Filtering + Pagination + Ordering

Real-world example:

```python
class BookListView(ListView):
    model = Book
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        qs = Book.objects.all().order_by('-created_at')

        genre = self.request.GET.get("genre")
        if genre:
            qs = qs.filter(genre=genre)

        return qs
```

---

## ⭐ Template Example (Bootstrap Cards)

```html
{% for book in books %}
<div class="card mb-3">
    <div class="card-body">
        <h5>{{ book.title }}</h5>
        <p>{{ book.author }}</p>
    </div>
</div>
{% empty %}
<p>No books found.</p>
{% endfor %}
```

---

## ⭐ Common Use Cases

ListView is ideal for:

* Blog homepage
* Product catalog
* Search results
* Admin dashboards
* User listings
* API pre-render pages

---

## ⭐ Advantages of ListView

✔ Less code
✔ Readable
✔ Maintainable
✔ Reusable
✔ Built-in features
✔ Industry standard

---

## ⚠️ Limitations

❌ Complex logic may require custom View
❌ Not ideal for heavy processing
❌ Learning curve for beginners

---

## 🧠 ListView vs TemplateView

| Feature         | TemplateView | ListView |
| --------------- | ------------ | -------- |
| Auto DB fetch   | ❌            | ✅        |
| Pagination      | ❌            | ✅        |
| Filtering hooks | ❌            | ✅        |
| Boilerplate     | More         | Less     |

---

## ⭐ Real-World Best Practice

Most production apps:

👉 Use ListView for read-only lists
👉 Override `get_queryset()` for logic
👉 Combine with filters & pagination

---

## 🚀 Pro Tips

* Always use `context_object_name`
* Prefer `get_queryset()` over raw queries in template
* Use pagination for large datasets
* Combine with search & filters
* Optimize queries using `select_related` / `prefetch_related`

---

## 🏁 Summary

ListView = **Professional way to display model lists in Django**

```
Minimal code + Powerful features + Clean architecture
```

👉 Essential for any Django backend developer

---

## 📌 Next Recommended Topics

* DetailView
* CreateView
* UpdateView
* DeleteView
* FormView
* Django REST Framework ViewSets

---

✨ You now have A-to-Z knowledge of ListView in Django 5

