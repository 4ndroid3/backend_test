from django.contrib import admin
from book.models import Library, Book, Author, Leads
# Register your models here.


admin.site.register(Library)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Leads)
