from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
MVC - MVT model view template

"""

def home(request):

    return HttpResponse('<h1>Blog home </h1>')
