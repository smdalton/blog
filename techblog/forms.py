from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

from markdownx.fields import MarkdownxFormField

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = models.UserProfile
        fields = '__all__'


class PostCreationForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = '__all__'


class MarkDownTestForm(forms.Form):
    markdown_field = MarkdownxFormField()
