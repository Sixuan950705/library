from django.contrib import admin
from mysite.models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','chapter','Publicationdate','body','pub_date')

admin.site.register(Book, BookAdmin)
