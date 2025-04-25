from .models import Book

book = Book.objects.get(title="1984")
book.title = "1984"
book.author = "Nineteen Eighty-Four"
book.save()

# Update book is 1984!
