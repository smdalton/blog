from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
# Register your models here.

from .models import Post, UserProfile

admin.site.header = "Blog Management Admin"

admin.site.register(Post, MarkdownxModelAdmin)
