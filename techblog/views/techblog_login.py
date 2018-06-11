from django.shortcuts import render


def techblog_login_page(request):
    return render(request, 'techblog_app/login.html')