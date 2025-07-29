from django.contrib import admin


from .models import Book
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("name", "surname")
    list_display = ("name", "surname")


class BookAdmin(admin.ModelAdmin):
    #readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author_name")


    def author_name(self, obj):
        return f"{obj.author.name} {obj.author.surname}"
    
    author_name.admin_order_field = "author__name"  # Optional: make sortable by author name
    author_name.short_description = "Author"
    

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
