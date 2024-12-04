from django.urls import path
from .views import list_books, LibraryDetailsView

urlpatterns = [
    path('list_book/', list_books, name='book_list'),
    path('library/', LibraryDetailsView.as_view(), name='library'),
]
