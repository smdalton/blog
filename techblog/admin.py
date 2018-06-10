from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import TestModel
# Register your models here.

from .models import Post, UserProfile

admin.site.header = "Blog Management Admin"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_post_title']

    def get_post_title(self, obj):
        return obj.headline


admin.site.register(TestModel, MarkdownxModelAdmin)
