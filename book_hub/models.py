from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField()
    rating = models.IntegerField()


    def __str__(self):
        return f"{self.title} (Rating: {self.rating})"