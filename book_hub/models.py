from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.name} {self.surname}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, db_index=True)


    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])


    def __str__(self):
        return f"title='{self.title}', author='{self.author}', rating={self.rating}, is_bestselling={self.is_bestselling}"

