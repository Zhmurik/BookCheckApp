from rest_framework import viewsets

from .models import Book, Reader
from .serializers import BooksSerializer, ReaderSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer


class ReaderViewSet(viewsets.ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
