from django import forms
from .models import Book

class BookCreationForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Book Name'
                }
            ),
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'published_on': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }