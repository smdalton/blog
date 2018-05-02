from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/profile_pictures',
                                        blank=True)
    bio = models.TextField(max_length=500, blank=True)


class Post(models.Model):
    headline = models.CharField(max_length=120)
    opening = models.CharField(max_length=1000)
    image = models.ImageField()
    content = models.CharField(max_length=5000)


