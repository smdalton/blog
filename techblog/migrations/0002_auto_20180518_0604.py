# Generated by Django 2.0.4 on 2018-05-18 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(blank=True, default='default value', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('O', 'Other'), ('T', 'Technology'), ('L', 'Lifestyle'), ('H', 'Health and Fitness'), ('F', 'Finance'), ('P', 'Projects'), ('C', 'Cooking'), ('H', 'Hiking'), ('G', 'Games'), ('PL', 'Plants')], default='O', max_length=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='post',
            name='headline_image',
            field=models.ImageField(blank=True, upload_to='media/blog_content/headline-photos'),
        ),
        migrations.AlterField(
            model_name='post',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='media/blog_content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='opening',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]