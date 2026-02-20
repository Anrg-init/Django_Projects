from django.db import models

# ==================================================
# DJANGO MODEL INHERITANCE – ALL TYPES IN ONE FILE
# ==================================================

# ==================================================
# 1. ABSTRACT BASE MODEL
# ==================================================
"""
CONCEPT:
- Parent model does NOT create a database table
- Used to share common fields
- Child models inherit fields directly
"""

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True   # ❌ no table created


class Student(BaseModel):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


"""
DATABASE TABLES:
- student
- teacher
❌ no table for BaseModel
"""

# ==================================================
# 2. MULTI-TABLE INHERITANCE
# ==================================================
"""
CONCEPT:
- Each model has its OWN database table
- Child model automatically gets OneToOneField to parent
- Used for real parent-child relationships
"""

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Employee(Person):
    employee_code = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.employee_code})"


"""
DATABASE TABLES:
- person
- employee (linked to person via OneToOneField)
"""

# ==================================================
# 3. PROXY MODEL
# ==================================================
"""
CONCEPT:
- NO new table is created
- Used to change behavior only
- Same data, different logic / ordering / admin
"""

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ActiveProduct(Product):
    class Meta:
        proxy = True      # ❌ no table created
        ordering = ["price"]

    def discounted_price(self):
        return self.price - 100


"""
DATABASE TABLES:
- product
❌ no table for ActiveProduct
"""

# ==================================================
# QUICK SUMMARY (MENTAL MODEL)
# ==================================================
"""
ABSTRACT MODEL:
- Reuse fields
- No table

MULTI-TABLE INHERITANCE:
- Parent + child tables
- Real relationship

PROXY MODEL:
- Same table
- Different behavior
"""
