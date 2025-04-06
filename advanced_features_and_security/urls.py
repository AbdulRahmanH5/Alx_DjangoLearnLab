from django.urls import path
from django.contrib.auth import views 
from .views import SignUpView, LogInView,LogOutView,profile_view
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('admin/', admin_view, name='admin' ),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
]


