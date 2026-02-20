# Django One-to-One Relationship (Complete A–Z Guide)

This single README covers **everything** about Django One-to-One relationships — concept, syntax, examples, signals, queries, errors, best practices — all in one place.

---

## 1. What is a One-to-One Relationship?

A **One-to-One relationship** means:
- One record in Model A is linked to **exactly one** record in Model B
- Model B is also linked to **only that one** record

### Examples
- User ↔ Profile  
- Student ↔ ID Card  
- Car ↔ Engine  

---

## 2. When to Use One-to-One?

Use One-to-One when:
- You want to **extend an existing model**
- Extra details should live in a separate table
- Each object must have **only one related object**

Do NOT use when:
- One object relates to many → use `ForeignKey`
- Many relate to many → use `ManyToManyField`

---

## 3. Basic Syntax

```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
