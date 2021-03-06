# Generated by Django 2.0.4 on 2018-06-12 04:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('main_image', models.ImageField(blank=True, upload_to='media/blog_content/main-image-photos')),
                ('content', markdownx.models.MarkdownxField()),
                ('category', models.CharField(blank=True, choices=[('DJBE', 'Django Backend'), ('DJFE', 'Django Frontend'), ('DJU', 'Django Utility'), ('T', 'Technology'), ('A', 'Algorithms'), ('MAKE', 'Arduino and Raspberry Pi'), ('CS', 'Computer Science Fundamentals'), ('PHYS', 'Physics'), ('MAT', 'Math')], default='O', max_length=4)),
                ('headline', models.CharField(blank=True, max_length=250)),
                ('headline_image', models.ImageField(blank=True, upload_to='media/blog_content/headline-photos')),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, default='default value', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, upload_to='static/profile_pictures')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
