from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Avg

from .models import Book


def book_hub_index(request):
    books = Book.objects.all().order_by("title") #.order_by("-rating") - For decending order
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))["rating__avg"]
    avg_rating = round(avg_rating, 2) if avg_rating is not None else 0.0
    return render(request, "book_hub/index.html", {
        "books": books,
        "total_books": total_books,
        "avg_rating": avg_rating,})


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(slug=slug)
    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_hub/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestselling": book.is_bestselling,
        })