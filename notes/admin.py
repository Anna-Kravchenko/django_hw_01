from django.contrib import admin
from .models import Category, Note


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'user', 'reminder')
    list_filter = ('category', 'user')
    search_fields = ('title', 'text')

admin.site.register(Category)
admin.site.register(Note)