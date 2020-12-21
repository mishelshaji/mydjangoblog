from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class':  'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class':  'form-control',
                    'rows': '4'
                }
            ),
            'body': forms.Textarea(
                attrs={
                    'class':  'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class':  'form-control'
                }
            ),
            'url': forms.TextInput(
                attrs={
                    'class':  'form-control'
                }
            )
        }