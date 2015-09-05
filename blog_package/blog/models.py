from django.contrib.auth.models import User
from django.db import models
from PIL import Image  # this is needed for the models.ImageField to work

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=False)
    body = models.ManyToManyField('Paragraph')
    date = models.DateField(auto_now_add=True)
    photos = models.ManyToManyField('Photo', blank=True)


class Photo(models.Model):
    blog_post = models.ForeignKey(Post, blank=True, null=True)
    title = models.CharField(max_length=30, blank=True, null=True)
    photo = models.ImageField(upload_to='profile_image/%Y/%m/%d', blank=True)
    date = models.DateField(auto_now_add=True)
    number = models.IntegerField(blank=True, null=True)


class Paragraph(models.Model):
    blog_post = models.ForeignKey(Post)
    paragraph = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)