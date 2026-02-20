# Django Model Many-to-Many Relationship (Complete A–Z Guide)

This single README explains **Django Many-to-Many relationships** completely — concept, syntax, examples, through tables, queries, admin usage, errors, and best practices — all in one place.

---

## 1. What is a Many-to-Many Relationship?

A **Many-to-Many relationship** means:
- Many objects of Model A relate to many objects of Model B
- Both sides can have multiple connections

In Django, this is implemented using **`ManyToManyField`**.

### Examples
- Students ↔ Courses  
- Posts ↔ Tags  
- Users ↔ Groups  
- Movies ↔ Actors  

---

## 2. When to Use Many-to-Many?

Use Many-to-Many when:
- One object can relate to **multiple objects**
- And those objects can relate back to **many objects**

Do NOT use when:
- Only one parent is allowed → `ForeignKey`
- Only one related object is allowed → `OneToOneField`

---

## 3. Basic Syntax

```python
class Course(models.Model):
    students = models.ManyToManyField(Student)
