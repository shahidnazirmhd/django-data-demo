from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book


def book_hub_index(request):
    books = Book.objects.all()
    return render(request, "book_hub/index.html", {"books": books})


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(slug=slug)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_hub/book_detail.html", {"book": book})