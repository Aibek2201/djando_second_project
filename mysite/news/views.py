import http
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello world</h1>")

def test(request):
    return HttpResponse('Test page')
