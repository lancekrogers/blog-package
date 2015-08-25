from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')


def resume(request):
    return HttpResponse('Resume Goes Here')


def projects(request):
    return HttpResponse("Example Projects Go Here")