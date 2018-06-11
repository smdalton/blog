from django.shortcuts import render


def home_from_techblog(request):
    print("compartmentalized views")
    return render(request, 'techblog_app/blog.html')