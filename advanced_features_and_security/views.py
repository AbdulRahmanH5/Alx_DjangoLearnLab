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
from django.contrib.auth.models import User

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
from .models import Book, User

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
        'users': User.objects.all(),
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
