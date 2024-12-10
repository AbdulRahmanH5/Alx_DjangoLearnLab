from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name= 'registration/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name= 'registration/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
]
