# Generated by Django 2.0.4 on 2018-06-10 18:50

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('techblog', '0002_auto_20180518_0604'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_text', markdownx.models.MarkdownxField()),
            ],
        ),
    ]