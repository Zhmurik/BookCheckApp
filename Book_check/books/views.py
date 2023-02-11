from rest_framework import viewsets

from .models import Book
from .serializers import BooksSerializer


class BookViewSet(viewsets.ModelViewSet):
    print("hello")
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
