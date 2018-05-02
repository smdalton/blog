from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return HttpResponse('You have reached the simple implementation of the home page')


def home_from_techblog(request):
    return HttpResponse('Homepage from techblog routes')


def posts(request):
    return render(request, 'homepage.html')
