from django.urls import path

from .views import APIBook, api_book_detail


urlpatterns = [
    path('books/', APIBook.as_view()),
    path('book/<int:pk>/', api_book_detail),
]