from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def resume(request):
    return render(request, 'portfolio/resume.html')


def projects(request):
    return render(request, 'portfolio/projects.html')

def edgar(request):
    return render(request, 'portfolio/edgar_project.html')
