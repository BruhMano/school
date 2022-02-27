from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request,id):
    post = Post.objects.get(id = id)
    return render(request,'post.html',{'post':post})
