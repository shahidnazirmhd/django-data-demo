from django.urls import path


from . import views


urlpatterns = [
    path("", views.book_hub_index, name="book_hub-index"),
    path("<slug:slug>/", views.book_detail, name="book-detail"),
]

