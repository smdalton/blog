from django.shortcuts import render


def techblog_login(request):
    return render(request, 'techblog_app/login.html')