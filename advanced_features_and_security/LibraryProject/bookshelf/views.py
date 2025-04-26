from django.shortcuts import render
from.models import Book
from django.contrib.auth.decorators import login_required, permission_required
from .forms import BookForm
from django.db.models import Q
# Create your views here.


@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@login_required
@permission_required('bookshelf.can_view', raise_exception=True)
def book_search(request):
    query = request.GET.get('q', '').strip()
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'books': books})
    
@login_required
@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            publication_year = form.cleaned_data['publication_year']
            Book.objects.create(
                title=title,
                author=author,
                publication_year=publication_year
            )
        else:
            form = BookForm()
    return render(request, 'bookshelf/book_create.html', {'form': form})


@login_required
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.publication_year = request.POST.get('publication_year')
        book.save()
    return render(request, 'bookshelf/book_edit.html', {'book': book})

@login_required
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
    return render(request, 'bookshelf/book_delete.html', {'book': book})