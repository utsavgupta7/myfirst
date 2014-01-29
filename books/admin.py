from django.contrib import admin
from books.models import publisher,author,books

admin.site.register(publisher)
admin.site.register(author)
admin.site.register(books)

