from .models import Book

# create.md
book = Book(title="1984",author= "George Orwell",publication_year= 1949)
book.save()
# Created a New book!

# retrieve.md
query = Book.objects.get()
# Created Objects (1)

# update.md
book = Book.objects.get(title="1984")
book.title = "1984"
book.author = "Nineteen Eighty-Four"
book.save()
# Update book is 1984!

# delete.md
book = Book.objects.get(title="1984")
book.delete()
# Deleted book 1984!
