from django.shortcuts import render
from django.http import HttpResponse
from . forms import MessageForm


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'projects/index.html', {'form': MessageForm()})

