from django.contrib import admin

from demo.models import Book, Album, Track, BookNumber, Character

# Register your models here.
# admin.site.register(Book)

admin.site.register(Album)
admin.site.register(Track)
admin.site.register(BookNumber)
admin.site.register(Character)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # it will display 'title', 'description' on the object list
    # fields = ['title', 'description', ]

    # it will display list 'title', 'price', 'description'
    list_display = ['title', 'price', 'description']

    # it will make a filter of 'is_published' or something we need
    list_filter = ['is_published', 'published']

    # it will make a search bar of 'title' or something we need
    search_fields = ['title', 'description']

