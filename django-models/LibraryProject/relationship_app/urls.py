from django.urls import path
from . import views

urlpatterns = [
    path('list_book/', views.book_list, name='book_list'),
    path('library/', views.LibraryDetailsView.as_view(), name='library'),
]
