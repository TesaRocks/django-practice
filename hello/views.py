from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "hello/index.html")


def tesa(request):
    return HttpResponse("hi Tes")


def rita(request):
    return HttpResponse("hi Rit")


def greet(request, name):
    return render(request, "Hello/greet.html", {name: name.capitalize()})
