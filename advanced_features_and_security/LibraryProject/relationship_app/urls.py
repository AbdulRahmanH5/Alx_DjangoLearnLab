from django.urls import path
from django.contrib.auth import views 
from .views import SignUpView, LogInView,LogOutView,profile_view
from .views import admin_view, librarian_view, member_view,book_list, LibraryDetailView, add_book, edit_book, delete_book

urlpatterns = [
    # Task 1
    path('books/', book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Task 2
    path('signup/', SignUpView.as_view(template_name = 'relationship_app/register.html'), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('profile/', profile_view, name='profile'),
    
    # Task 3
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
    
    # Task 4
    path('add/', add_book, name='add_book'),
    path('edit/', edit_book, name='edit_book'),
    path('delete/', delete_book, name='delete_book'),
]


