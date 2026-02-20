from . import models
from django.forms import forms


class ProductForm(forms.ModelForm):
    class meta:
        model = models.Product
        fields = '__all__'

        