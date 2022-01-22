from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.
posts = [
    {
        'author':'abc',
        'title':'Post 1',
        'content':'def',
        'date':'Jan 21'
    },
    {
        'author':'def',
        'title':'Post 1',
        'content':'ghi',
        'date':'Jan 22'
    }
]
def home(request):
    context = {
        'posts':post.objects.all,
        'title':"Home"
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')