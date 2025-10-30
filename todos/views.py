from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('hello world')
    # return HttpResponse("<h1> Hello World </h1>")
    return render(request, 'todos/home.html')
