from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import BookViewSet


router = SimpleRouter()
router.register('books', BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
