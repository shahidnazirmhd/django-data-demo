from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, editable=False, blank=True) # Makes the field unique; also auto-indexed (db_index=True)


    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
    # Check if the object is new or title changed
        if not self.slug or self._title_changed():
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Book.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def _title_changed(self):
        if not self.pk:
            return True  # New object, title "changed" by default
        old_title = Book.objects.get(pk=self.pk).title
        return old_title != self.title


    def __str__(self):
        return f"title='{self.title}', author='{self.author}', rating={self.rating}, is_bestselling={self.is_bestselling}"

