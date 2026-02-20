# Django Model Inheritance (ALL TYPES)

Django provides **3 main types of model inheritance** that help you structure your database models efficiently.

## Types of Model Inheritance

1. **Abstract Base Model**
2. **Multi-Table Inheritance**
3. **Proxy Model**

This README explains **all three**, with **one single `models.py` example**.

---

## models.py

```python
from django.db import models

# ==================================================
# 1. ABSTRACT BASE MODEL
# ==================================================
"""
Concept:
- Parent model does NOT create a database table
- Child models reuse fields
- Best for common fields (created_at, updated_at, etc.)
"""

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True   # makes it abstract


class Student(TimeStampModel):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(TimeStampModel):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


"""
DB Tables Created:
- student
- teacher
❌ NO table for TimeStampModel
"""

# ==================================================
# 2. MULTI-TABLE INHERITANCE
# ==================================================
"""
Concept:
- Each model gets its OWN database table
- Child has OneToOneField link to parent automatically
- Use when child is a specialized version of parent
"""

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(Person):
    employee_id = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.employee_id})"


"""
DB Tables Created:
- person
- employee (linked via OneToOneField)
"""

# ==================================================
# 3. PROXY MODEL
# ==================================================
"""
Concept:
- NO new table created
- Used to change behavior (methods, ordering, admin)
- Same database table as original model
"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ActiveProduct(Product):

    class Meta:
        proxy = True   # proxy model
        ordering = ["price"]

    def discounted_price(self):
        return self.price - 100


"""
DB Tables Created:
- product
❌ NO table for ActiveProduct
"""
