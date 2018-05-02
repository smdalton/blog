from django.http import HttpResponse
from django.shortcuts import render


def landing(request):
    return HttpResponse('This is the generic landing page')