from django.shortcuts import render, redirect
from techblog.forms import PostCreationForm


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
