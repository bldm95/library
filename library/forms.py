from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'year_of_publication', 'description', 'image')


class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'author', 'year_of_publication', 'description', 'image')
