from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
# Create your models here.
DJANGO = 'Django'





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='static/profile_pictures', blank=True)
    bio = models.TextField(max_length=500, blank=True)


class Post(models.Model):
    POST_CHOICES = (
        ('DJBE', 'Django Backend'),
        ('DJFE', 'Django Frontend'),
        ('DJU', 'Django Utility'),
        ('T', 'Technology'),
        ('A', 'Algorithms'),
        ('MAKE', 'Arduino and Raspberry Pi'),
        ('CS', 'Computer Science Fundamentals'),
        ('PHYS', 'Physics'),
        ('MAT', 'Math')
    )
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='default value', blank=True)
    main_image = models.ImageField(upload_to='media/blog_content', blank=True)
    content = MarkdownxField()
    category = models.CharField(max_length=4, default='O', choices=POST_CHOICES, blank=True)
    # Headline is for the display card
    headline = models.CharField(max_length=250, blank=True)
    headline_image = models.ImageField(upload_to='media/blog_content/headline-photos', blank=True)
    date = models.DateTimeField(auto_now=True)

    @property
    def formatted_markdown(self):
        return markdownify(self.content)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
