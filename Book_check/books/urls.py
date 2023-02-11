from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import BookViewSet, ReaderViewSet


router = SimpleRouter()
router.register('books', BookViewSet)
router.register('reader', ReaderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
