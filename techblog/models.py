from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/profile_pictures',blank=True)
    bio = models.TextField(max_length=500, blank=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='default value')
    # Headline is for the display card
    headline = models.CharField(max_length=120)
    headline_image = models.ImageField(upload_to='media/blog_content/headline-photos', blank=False)
    opening = models.CharField(max_length=500)
    image1 = models.ImageField(upload_to='media/blog_content')
    image2 = models.ImageField(upload_to='media/blog_content')
    image3 = models.ImageField(upload_to='media/blog_content')
    image4 = models.ImageField(upload_to='media/blog_content')
    image5 = models.ImageField(upload_to='media/blog_content')
    content = models.CharField(max_length=5000)

