from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = models.UserProfile
        fields = '__all__'


class PostCreationForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = '__all__'
