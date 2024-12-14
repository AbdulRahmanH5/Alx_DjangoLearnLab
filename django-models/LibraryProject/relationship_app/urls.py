from django.urls import path
from django.contrib.auth import views 
from .views import SignUpView, LogInView,LogOutView,profile_view
from .views import admin_view, librarian_view, member_view,book_list, LibraryDetailView

urlpatterns = [
    # Task 1
    path('books/', book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Task 2
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    
    #task 3
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
]


