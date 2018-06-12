from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.management import call_command
from techblog import models
from faker import Faker
from .structures import choices_map

class Command(BaseCommand):

    def __init__(self):
        self.fake = Faker()

    def create_admin(self):
        user = User.objects.create_user('Shane', password='pass1234')
        user.is_superuser = True
        user.is_staff = True
        user.first_name = 'Shane'
        user.last_name = 'Dalton'
        user.email = 'shanemdalton@gmail.com'
        user.save()

    # create  a single post of type category
    def create_post(self, category):
        fake = self.fake
        post = models.Post(
            title=fake.sentence(),
            author=User.objects.get(first_name='Shane'),
            content=fake.paragraph(),
            category=category,
            headline=fake.sentence(),
        )
        post.save()

    def create_posts(self):
        # make a post for eac
        for key in choices_map:
            self.create_post(key)


