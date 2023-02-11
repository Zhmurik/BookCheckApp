from rest_framework import serializers
from .models import Book, Reader


class BooksSerializer(serializers.ModelSerializer):
    reader = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field='user_name',
                                          )

    class Meta:
        model = Book
        fields = ('book_name', 'author', 'year_published', 'genres', 'reader')


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(many=True,
                                         read_only=True,
                                         slug_field='book_name')

    class Meta:
        model = Reader
        fields = ('first_name', 'last_name', 'user_name', 'books')
