## 📌 Namespace in Django (URLs)

**Namespace = a label for a group of URLs**

It helps Django distinguish between URLs that have the **same name** but belong to different apps.

---

## ❓ Why Namespace is Needed

Multiple apps can have the same URL name:

```
accounts app → name="login"
admin app    → name="login"
shop app     → name="login"
```

Without namespace → Django gets confused ❌
With namespace → Clear identification ✅

---

## 📌 How to Define Namespace

### Step 1 — In app's `urls.py`

```
# accounts/urls.py
app_name = "accounts"

urlpatterns = [
    path("login/", views.login_view, name="login"),
]
```

`app_name` = namespace name

---

### Step 2 — Include in main `urls.py`

```
path("accounts/", include("accounts.urls"))
```

---

## 📌 How to Use Namespace

### In templates

```
<a href="{% url 'accounts:login' %}">Login</a>
```

Format:

```
namespace:url_name
```

---

### In views (reverse)

```
from django.urls import reverse

reverse("accounts:login")
```

---

## 📌 Real Example with Two Apps

```
accounts → login
admin    → login
```

Use:

```
accounts:login
admin:login
```

Now Django knows exactly which one.

---

## 📌 Without Namespace (Problem)

```
name="login"
```

Django error:

```
Reverse for 'login' not found OR ambiguous
```

---

## 📌 Key Points (Very Important)

✔ Namespace = app_name
✔ Prevents URL name conflicts
✔ Used with `include()`
✔ Format: `namespace:url_name`
✔ Works in templates + views

---

## 🧠 One-Line Definition

> Namespace uniquely identifies URL names of an app in Django.

---

If you want, I can next explain:

* 🔥 URL routing flow in Django (from request to view)
* 🔥 reverse() vs redirect() vs resolve()
* 🔥 include() deep explanation
* 🔥 Complete URL dispatcher A-to-Z

Just say **NEXT**.
