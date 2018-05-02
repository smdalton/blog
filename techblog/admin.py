from django.contrib import admin

# Register your models here.

from .models import Post, UserProfile

class PostAdmin(admin.ModelAdmin):

class UserProfileAdmin(admin.ModelAdmin):



admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile, UserProfileAdmin)