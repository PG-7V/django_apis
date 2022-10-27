from django.views.generic import ListView

from apps.books.models import Book


class BookListView(ListView):
    model = Book
    template = 'book_list.html'
