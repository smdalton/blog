from django.http import HttpResponse


def home(request):
    return HttpResponse('You have reached the simple implementation of the home page')
