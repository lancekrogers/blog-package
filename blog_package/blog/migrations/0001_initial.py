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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, null=True, max_length=30)),
                ('photo', models.ImageField(blank=True, upload_to='profile_image/%Y/%m/%d')),
                ('date', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('body', models.ManyToManyField(to='blog.Paragraph')),
                ('photos', models.ManyToManyField(to='blog.Photo', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='blog_post',
            field=models.ForeignKey(null=True, to='blog.Post', blank=True),
        ),
        migrations.AddField(
            model_name='paragraph',
            name='blog_post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
