from rest_framework import generics

from apps.api.serializers import BookSerializer
from apps.books.models import Book


class BookApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
