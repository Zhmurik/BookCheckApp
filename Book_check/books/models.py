from django.db import models


class Reader(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.user_name}'


class Book(models.Model):
    book_name = models.CharField(max_length=200,
                                 verbose_name='Book name',
                                 db_index=True,
                                 )
    author = models.CharField(max_length=200,
                              verbose_name='Author',
                              )
    year_published = models.CharField(max_length=30,
                                      verbose_name='Originally published',
                                      )
    GENRES_TYPES = (
        (1, 'Classics'),
        (2, 'Action and Adventure'),
        (3, 'Fantasy'),
        (4, 'Horror'),
        (5, 'Novel'),
        (6, 'Historical Fiction'),
        (7, 'Dystopian'),
        (8, 'Detective and Mystery')
    )
    genres = models.IntegerField(verbose_name='Genres',
                                 choices=GENRES_TYPES,
                                 )
    description = models.CharField(max_length=500,
                                   verbose_name='Book description')
    reader = models.ManyToManyField(Reader,
                                    related_name='books')
