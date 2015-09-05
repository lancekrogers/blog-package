from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def makepost(request):
    return render(request, 'blog/post-creation.html')