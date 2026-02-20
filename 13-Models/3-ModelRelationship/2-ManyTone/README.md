# Django Model Many-to-One Relationship (Complete A–Z Guide)

This single README explains **Django Many-to-One relationships** (using `ForeignKey`) completely — concept, syntax, examples, queries, deletes, errors, and best practices — all in one place.

---

## 1. What is a Many-to-One Relationship?

A **Many-to-One relationship** means:
- Many objects of one model relate to **one object** of another model

In Django, this is implemented using **`ForeignKey`**.

### Examples
- Many Posts → One Author  
- Many Students → One Class  
- Many Orders → One Customer  
- Many Comments → One Blog  

---

## 2. When to Use Many-to-One?

Use Many-to-One when:
- One parent object can have **multiple child objects**
- Child objects belong to **only one parent**

Do NOT use when:
- One-to-one mapping is needed → `OneToOneField`
- Many objects relate to many → `ManyToManyField`

---

## 3. Basic Syntax

```python
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
