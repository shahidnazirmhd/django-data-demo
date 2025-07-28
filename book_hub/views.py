from django.shortcuts import render

from .models import Book


def book_hub_index(request):
    books = Book.objects.all()
    return render(request, "book_hub/index.html", {"books": books})


def book_detail(request, slug):
    return render(request, "book_hub/book_detail.html",)