from .models import Author,Book,Library,Librarian

# Query all books by a specific author.
def get_all_books_by_author():
    author = Author.objects.get(name = 'Ali Hassan')
    books = Book.objects.filter(author=author)
    return books

# List all books in a library.
def get_all_books_in_library():
    library = Library.objects.get(name= 'Alnahda')
    books = library.books.all()
    return books

# Retrieve the librarian for a library.
def get_librarian_for_library():
    library = Library.objects.get(name = 'Alrooda')
    librarian = Librarian.objects.get(library=library)
    return librarian