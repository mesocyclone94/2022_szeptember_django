from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
MVC - MVT model view template

"""

posts = [
    {
        'author':'Akli Miklós',
        'title':'blog post 1',
        'content':'first_content',
        'date_posted':'2022 szeptember 12'
    },
    {
        'author':'Akli Miklós',
        'title':'blog post 2',
        'content':'second_content',
        'date_posted':'2022 szeptember 15'
    },
    {
        'author':'Akli Miklós',
        'title':'blog post 3',
        'content':'third_content',
        'date_posted':'2022 szeptember 13'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')