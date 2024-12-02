from django.db import models

# Create your models here.

# Author Model.
class Author(models.Model):
    name = models.CharField(max_length=30)
    
# Book Model.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
# Library Model.
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='librares')
    
# Librarian Model.
class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)