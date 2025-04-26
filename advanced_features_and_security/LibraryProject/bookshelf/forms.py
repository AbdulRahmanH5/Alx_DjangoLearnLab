from django import forms
from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_year = forms.IntegerField(required=True)

class ExampleForm(forms.Form):
    example_field = forms.CharField(max_length=100, required=True)
    another_field = forms.IntegerField(required=True)
