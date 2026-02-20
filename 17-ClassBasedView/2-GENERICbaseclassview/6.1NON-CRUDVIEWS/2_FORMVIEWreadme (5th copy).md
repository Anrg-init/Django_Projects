```md
# Django 5 Generic Class-Based Views — Deep Mastery Series

## 📍 PART 7 — FormView (Forms NOT tied to a Model)

⚠️ VERY IMPORTANT for real apps (login, contact, search, OTP, etc.)

If CreateView = Form + Model save  
👉 FormView = Form only (YOU decide what happens)

---

# 🧠 What is FormView?

**FormView displays and processes a form that is NOT automatically saved to the database.**

---

## 🌐 Real Website Examples

| Feature | Why FormView |
|----------|--------------|
Contact form | Send email |
Login form (custom) | Authenticate user |
Search form | Filter results |
OTP verification | Validate code |
Newsletter signup | Send to API |
Feedback form | Custom processing |

---

# 🧩 One-Line Definition

> FormView handles form display and processing without automatic model saving.

---

# ⚙️ Step 1 — Create a Form (NOT ModelForm)

## forms.py

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

👉 Uses `forms.Form` (not ModelForm)

---

# ⚙️ Step 2 — Create View

```python
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/thanks/"
```

---

# ⚙️ Step 3 — URL

```python
path("contact/", ContactView.as_view(), name="contact")
```

---

# 📄 Template

```html
<h1>Contact Us</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
```

---

# 🔥 What Django Automatically Does

## 🟢 GET request

👉 Shows empty form

## 🔵 POST request

👉 Validates form  
👉 If valid → form_valid()  
👉 If invalid → form_invalid()  
👉 Redirect to success_url (if valid)

---

# 🧠 Why NOT ModelForm?

Because many forms don’t save data directly.

Examples:

- Login form
- Email form
- Search form
- OTP verification
- Payment form

---

# 📦 Template Context Variables

## ⭐ Main variable

```
form
```

---

# ⚙️ Core Attributes (A-to-Z)

---

## ✅ template_name

Form page template.

---

## ✅ form_class (REQUIRED)

Your form definition.

---

## ✅ success_url

Where to redirect after success.

---

## ✅ initial

Pre-fill form fields.

```python
initial = {"name": "Guest"}
```

---

# 🧩 MOST IMPORTANT METHODS

---

## ⭐ form_valid(self, form)  🔥🔥🔥

Runs AFTER validation succeeds.

👉 THIS is where your app logic goes.

---

### Example — Debugging

```python
def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
```

Output appears in terminal.

---

## 🧠 What is cleaned_data?

Validated + safe user input.

Example:

```python
{
  "name": "Anurag",
  "email": "a@gmail.com",
  "message": "Hello"
}
```

---

## ⭐ REAL USE CASES

---

### ✅ Send email

```python
from django.core.mail import send_mail

def form_valid(self, form):
    send_mail(
        "Contact Message",
        form.cleaned_data["message"],
        form.cleaned_data["email"],
        ["admin@example.com"]
    )
    return super().form_valid(form)
```

---

### ✅ Save to database manually

```python
def form_valid(self, form):
    data = form.cleaned_data

    Feedback.objects.create(
        name=data["name"],
        email=data["email"],
        message=data["message"]
    )

    return super().form_valid(form)
```

---

### ✅ Login system

```python
from django.contrib.auth import authenticate, login

def form_valid(self, form):
    user = authenticate(
        username=form.cleaned_data["username"],
        password=form.cleaned_data["password"]
    )
    login(self.request, user)
    return super().form_valid(form)
```

---

### ✅ Call external API

```python
import requests

def form_valid(self, form):
    requests.post("https://api.site.com", data=form.cleaned_data)
    return super().form_valid(form)
```

---

## ⭐ form_invalid(self, form)

Runs when validation fails.

```python
def form_invalid(self, form):
    print(form.errors)
    return super().form_invalid(form)
```

---

## ⭐ get_context_data()

Add extra template variables.

---

## ⭐ get_initial()

Pre-fill fields dynamically.

```python
def get_initial(self):
    return {"name": self.request.user.username}
```

---

# ⚡ Request Flow (End-to-End)

### Step 1 — User opens page

GET → empty form shown

---

### Step 2 — User submits

POST → validation runs

---

### Step 3 — If valid

✔️ form_valid() executes  
✔️ Redirect to success_url  

---

### Step 4 — If invalid

❌ Errors shown on same page  

---

# 🧠 Internal Mechanics (Deep Concept)

FormView combines:

```
FormMixin
ProcessFormView
TemplateResponseMixin
View
```

---

# ❌ Common Mistakes

### ❌ Expecting auto-save

FormView does NOT save anything.

---

### ❌ Forgetting success_url

Redirect fails.

---

### ❌ Using ModelForm unnecessarily

Use CreateView instead.

---

### ❌ Not returning super().form_valid()

Breaks redirect flow.

---

# 🆚 FormView vs CreateView

| Feature | FormView | CreateView |
|----------|-----------|-------------|
Auto save model | ❌ No | ✅ Yes |
Requires model | ❌ No | ✅ Yes |
Use case | Custom processing | Add DB record |

---

# 🚀 Real Project Uses

- Contact forms
- Login forms
- Password reset flows
- OTP verification
- Search forms
- Payment forms
- Newsletter signup
- Settings forms

---

# 🏁 FINAL SUMMARY

👉 FormView handles forms without automatic DB saving  
👉 YOU control what happens after submission  
👉 Extremely flexible  
👉 Used everywhere in real apps  

---

# 📌 MASTER ONE-LINE MEMORY

> FormView displays and processes a form not tied to a model.

```

---

## ✅ Your move

Reply ONE:

- **"Next"** → RedirectView (very useful but simple)
- **"Practice tasks"**
- **"Test me"**
- **"Explain differences between all views"**
- Ask doubts

I’ll guide you 👍
