from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'id')
    search_fields = ('title', 'body')

