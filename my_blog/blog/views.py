from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
MVC - MVT model view template

"""

def home(request):

    return HttpResponse('<h1>Blog home valami</h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')