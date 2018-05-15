from django.http import HttpResponse
from django.shortcuts import render


def landing(request):
    """
        Landing page will contain
    """
    return render(request, 'techblog_app/homepage.html')


def projects(request):
    return render(request, 'techblog_app/projects.html')

def about(request):
    return render(request, 'techblog_app/about.html')
