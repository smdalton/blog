from django.http import HttpResponse
from django.shortcuts import render, redirect
from techblog.forms import MarkDownTestForm


def markdown_test(request):

    if request.method == 'GET':
        form = MarkDownTestForm()
        return render(request,'techblog_app/markdownform.html',{'form':form})

    elif request.method == 'POST':
        print('incoming form data')
    return HttpResponse('url test success')