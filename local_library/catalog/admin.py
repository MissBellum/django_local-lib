from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


class AuthorInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    #exclude = ('date_of_birth', 'date_of_death')
    inlines = [AuthorInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
    
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'summary')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'id', 'borrower', 'due_back', 'status')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'id', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
   
   
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
