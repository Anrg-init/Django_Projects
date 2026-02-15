from django import forms
from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'description',
            'genre',
            'isbn',
            'publication_date'
        ]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title'
            }),

            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter author name'
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write book description...',
                'rows': 4
            }),

            'genre': forms.Select(attrs={
                'class': 'form-control'
            }),

            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter ISBN number'
            }),

            'publication_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
