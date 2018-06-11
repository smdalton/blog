from django.http import HttpResponse
from django.shortcuts import render
from techblog.models import Post

def posts(request):

    posts = Post.objects.get(pk=1)
    print(posts)
    if posts:
        return render(
            request,
            'techblog_app/view_posts.html',
            {
                'post': posts
            }
        )