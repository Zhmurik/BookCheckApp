from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Book
from .serializers import BooksSerializer


class APIBook(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_book_detail(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'PUT' or request.method == 'PATCH':
        serializer = BooksSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=204)
    serializer = BooksSerializer(book)
    return Response(serializer.data)
