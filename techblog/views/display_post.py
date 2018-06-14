from django import template
from django.http import HttpResponse
from django.shortcuts import render
from techblog.models import Post


def display_post(request, post_id):

    # get the post with the indicated id
    post = Post.objects.get(id=post_id)

    return render(
        request,
        'techblog_app/view_single_post.html',
        {
            'post': post
        })