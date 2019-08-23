from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    with open('counter', 'r') as f:
        counter = f.read()
    return HttpResponse('COUNTER: ' + counter)