from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.management import call_command
from techblog import models
from faker import Faker
from .structures import choices_map
from blog.settings import BASE_DIR
from django.core.files import File
import os, sys, glob
from blog.settings import BASE_DIR


class Command(BaseCommand):

    def __init__(self):
        self.fake = Faker()
        self.debug_picture= os.getcwd() + '/media/populate/IMG_1211.JPG'
        print(self.debug_picture)
    def create_admin(self):
        # if the admin already exists ignore the error about uniqueness
        try:
            user = User.objects.create_user('Shane', password='pass1234')
            user.is_superuser = True
            user.is_staff = True
            user.first_name = 'Shane'
            user.last_name = 'Dalton'
            user.email = 'shanemdalton@gmail.com'
            user.save()
        except :
            print(f"admin already exists, exception handled: ")

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
        post.headline_image.save(category, File(open(self.debug_picture, 'rb')))
        post.main_image.save(category, File(open(self.debug_picture, 'rb')))
        post.save()

    def create_posts(self):
        # make a post for eac
        for key in choices_map:
            self.create_post(key)

    # delete the sqlite file

    def handle(self, **args):
        self.create_admin()
        self.create_posts()

