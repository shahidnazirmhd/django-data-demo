from django.contrib import admin


from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    # prepopulated_fields = {"slug": ("title",)}     #No need, since using custom auto populated unique slug generation
    list_filter = ("author", "rating")
    list_display = ("title", "author")

admin.site.register(Book, BookAdmin)
