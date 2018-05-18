from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import PostCreationForm
# Create your views here.


def home(request):
    return HttpResponse('You have reached the simple implementation of the home page')


def home_from_techblog(request):
    return render(request, 'techblog_app/blog.html')


def techblog_post(request):

    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/techblog')
    else:

        form = PostCreationForm()
        args = {'form': form}
    return render(request, 'techblog_app/post.html', args)


def techblog_login_page(request):
    return render(request, 'techblog_app/login.html')



# Create a User Account Here
def techblog_signup_page(request):

    if request.method == 'POST':
        # process the form
        form = UserCreationForm(request.POST)
        form.save()
        return redirect('/techblog')

    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'techblog_app/signup.html', args)

    return render(request, 'techblog_app/signup.html')
