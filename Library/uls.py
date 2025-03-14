from django.urls import path
from .views import AddBookAllBooks, SearchBook

urlpatterns = [
    path('Books/', AddBookAllBooks.as_view()),
    path('Books/<str:author>/', SearchBook.as_view())
]