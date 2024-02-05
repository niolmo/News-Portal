from django.contrib import admin

from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publ', 'status']
    list_filter = ['status', 'created', 'publ', 'author']
    search_fields = ['title', 'text']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publ'
    ordering = ['status', 'publ']


@admin.register(Commetns)
class CommetnsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['name', 'email', 'body']
