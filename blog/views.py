from django.http import HttpResponse
from django.shortcuts import render


def landing(request):
    """
        Landing page will contain
    """
    return render(request, 'techblog_app/homepage.html')