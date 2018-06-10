from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField

# Create your models here.
CATEGORIES = (
    ('O', 'Other'),
    ('T', 'Technology'),
    ('L', 'Lifestyle'),
    ('H', 'Health and Fitness'),
    ('F', 'Finance'),
    ('P', 'Projects'),
    ('C', 'Cooking'),
    ('H', 'Hiking'),
    ('G', 'Games'),
    ('PL', 'Plants')
)

class TestModel(models.Model):
    test_text = MarkdownxField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/profile_pictures', blank=True)
    bio = models.TextField(max_length=500, blank=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='default value', blank=True)
    # Headline is for the display card
    category = models.CharField(max_length=4, default='O', choices=CATEGORIES, blank=True)
    headline = models.CharField(max_length=250, blank=True)
    headline_image = models.ImageField(upload_to='media/blog_content/headline-photos', blank=True)
    opening = models.CharField(max_length=500, blank=True)
    main_image = models.ImageField(upload_to='media/blog_content', blank=True)
    content = models.CharField(max_length=5000, blank=True)
    date = models.DateTimeField(auto_now=True)

