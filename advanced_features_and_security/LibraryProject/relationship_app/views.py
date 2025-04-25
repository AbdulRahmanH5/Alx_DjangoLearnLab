from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import TemplateView
from .models import Book, Librarian, Author
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Library
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from django.conf import settings

# Task 1
def book_list(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    context = {
        'book_list': books,
        'author': authors
    }
    return render(request, 'relationship_app/book_list.html', context)
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all() 
        return context

# Task 2
class HomeView(TemplateView):
    template_name = 'relationship_app/home.html'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'
    
class LogInView(LoginView):
    template_name = 'relationship_app/login.html'
    
class LogOutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    
@login_required
def profile_view(requets):
    return render(requets, 'relationship_app/profile.html')


# Task 03
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'admin'

def is_librarian(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'librarian'

def is_member(user):
    return user.is_authenticated and getattr(user, 'role', None) == 'member'


@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    context = {
        'books': Book.objects.all(),
        'users': settings.AUTH_USER_MODEL.objects.all(),
        'total_books': Book.objects.count()
    }
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    context = {
        'books': Book.objects.all(),
        'borrowed_books': Book.objects.filter(is_borrowed=True),
        'available_books': Book.objects.filter(is_borrowed=False)
    }
    return render(request, 'relationship_app/librarian_view.html', context)

@user_passes_test(is_member, login_url='login')
def member_view(request):
    context = {
        'borrowed_books': Book.objects.filter(borrowed_by=request.user),
        'available_books': Book.objects.filter(is_borrowed=False)
    }
    return render(request, 'relationship_app/member_view.html', context)


# Task 4
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html',{'form':form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
        
    return render(request, 'relationship_app/can_edit_book.html',{'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/can_delete_book.html',{'book': book})