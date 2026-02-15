# Django 5 — FormView (Generic Class-Based View) — A to Z Guide

## 📌 What is FormView?

**FormView** is used to display and process a form that is NOT directly tied to a model.

👉 Example:

- Contact form
- Login form (custom)
- Feedback form
- Search form
- OTP verification form
- Newsletter signup

If CreateView = Form + Model save  
Then FormView = Form only (you decide what to do)

---

## 🧠 Real Website Examples

| Website | Form |
|----------|------|
Contact Us page | Send message |
Search box page | Search data |
Forgot password | Send email |
Feedback page | Submit feedback |

---

## 📦 Import

```python
from django.views.generic.edit import FormView
🏗️ Basic Setup (Step-by-Step)
1️⃣ Create Form
python
Copy code
# forms.py

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
👉 Note: Uses forms.Form, NOT ModelForm

2️⃣ View
python
Copy code
# views.py

from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/thanks/"
3️⃣ URL
python
Copy code
# urls.py

from django.urls import path
from .views import ContactFormView

urlpatterns = [
    path("contact/", ContactFormView.as_view(), name="contact"),
]
4️⃣ Template
html
Copy code
<!-- contact.html -->

<h1>Contact Us</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Send</button>
</form>
⚙️ What Happens Internally
GET request
👉 Shows empty form

POST request
👉 Validates form
👉 If valid → calls form_valid()
👉 If invalid → calls form_invalid()

🔑 Important Attributes (A to Z)
✅ template_name
Form page template.

python
Copy code
template_name = "contact.html"
✅ form_class
Your form class.

python
Copy code
form_class = ContactForm
✅ success_url
Where to redirect after success.

python
Copy code
success_url = "/thanks/"
✅ initial
Pre-fill form fields.

python
Copy code
initial = {"name": "Guest"}
🧩 Most Important Methods
✅ form_valid(self, form)
Runs when form is valid.

👉 You handle what happens after submission.

python
Copy code
def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)
🔹 Example — Send Email
python
Copy code
def form_valid(self, form):
    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    message = form.cleaned_data["message"]

    # Example action
    print(name, email, message)

    return super().form_valid(form)
✅ form_invalid(self, form)
Runs when validation fails.

python
Copy code
def form_invalid(self, form):
    print("Form errors:", form.errors)
    return super().form_invalid(form)
🧠 Access Submitted Data
Use:

python
Copy code
form.cleaned_data
Example:

python
Copy code
name = form.cleaned_data["name"]
🧪 Full Working Example
forms.py
python
Copy code
class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100)
    rating = forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea)
views.py
python
Copy code
class FeedbackView(FormView):
    template_name = "feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        data = form.cleaned_data

        print("Name:", data["name"])
        print("Rating:", data["rating"])
        print("Comment:", data["comment"])

        return super().form_valid(form)
template
html
Copy code
<h2>Feedback Form</h2>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button>Submit</button>
</form>
⚡ Request Flow
🟢 GET
User opens page

Empty form shown

🔵 POST
User submits form

Form validation runs

If valid → form_valid()

Redirect to success_url

🧩 Add Extra Context
Use get_context_data()

python
Copy code
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["title"] = "Contact Page"
    return context
Template:

html
Copy code
<h1>{{ title }}</h1>
🆚 FormView vs CreateView
Feature	FormView	CreateView
Model required	❌ No	✅ Yes
Saves object	❌ Manual	✅ Automatic
Use case	Custom forms	Add new database record

❌ Common Mistakes
❌ Using ModelForm with FormView
Better use CreateView for model saving.

❌ Forgetting success_url
Without it, redirect fails.

❌ Not handling form_valid()
Nothing useful happens.

🚀 Advanced Use Cases
Send email forms

OTP verification

Payment forms

Search filters

Settings forms

Newsletter signup

File upload forms
