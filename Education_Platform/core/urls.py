from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView

# url patterns for the application
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)