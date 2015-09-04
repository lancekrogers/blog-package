# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('paragraph', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, blank=True, max_length=30)),
                ('photo', models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('date', models.DateField(auto_now_add=True)),
                ('body', models.ManyToManyField(to='blog.Paragraph')),
                ('photos', models.ManyToManyField(to='blog.Photo')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='blog_post',
            field=models.ForeignKey(to='blog.Post', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='blog_post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
