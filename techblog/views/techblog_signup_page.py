from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


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