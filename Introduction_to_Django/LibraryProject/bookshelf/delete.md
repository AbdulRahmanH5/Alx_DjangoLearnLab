from bookshelf.models import Book
book = Book.objects.get(title="1984")
book.delete()
# Deleted book 1984!
