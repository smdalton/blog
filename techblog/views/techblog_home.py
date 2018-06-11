from django.shortcuts import render

from techblog import models


def techblog_home(request):

    # get the posts from the backend
    posts = models.Post.objects.all()
    # sort them by date

    print("compartmentalized views")
    return render(
        request,
        'techblog_app/techblog_home.html',
        {
            'posts':posts
        }
    )