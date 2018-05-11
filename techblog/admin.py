from django.contrib import admin

# Register your models here.

from .models import Post, UserProfile

admin.site.header = "Blog Management Admin"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_post_title']

    def get_post_title(self, obj):
        return obj.headline

