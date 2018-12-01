from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
    return HttpResponse(content='Hello, Naveen!<br>How\'s the day going on?')


