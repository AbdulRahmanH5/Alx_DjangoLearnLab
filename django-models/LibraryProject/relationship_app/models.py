from django.db import models

# Create your models here.

# Author Model.
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
# Book Model.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author}"
    
# Library Model.
class Library(models.Model):
    name = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='librares')

    def __str__(self):
        return self.name
    
# Librarian Model.
class Librarian(models.Model):
    name = models.CharField(max_length=30)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
