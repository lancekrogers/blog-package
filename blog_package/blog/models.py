from django.contrib.auth.models import User
from django.db import models
from PIL import Image  # this is needed for the models.ImageField to work

# Create your models here.



class Post(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=60, blank=False)
    body = models.TextField(blank=True, null=True)


class Photo(models.Model):
    title = models.CharField(max_length=30, blank=True)
    photo = models.ImageField()

