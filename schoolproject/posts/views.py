from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from like.models import Like
from .forms import NewPostForm

def index(request):
    likes = Like.objects.all()
    posts = Post.objects.all()
    for post in posts:
        post.likes = Like.objects.filter(post=post).all().__len__()
        try:
                like = Like.objects.get(post=post,user=request.user)
        except Exception as e:
                like = None
        if like in likes:
                post.is_liked_by_current_user = True
        else:
                post.is_liked_by_current_user = False
    return render(request, 'index.html', {'posts': posts})

def post(request,id):
    likes = Like.objects.all()
    post = Post.objects.get(id = id)
    post.likes = Like.objects.filter(post=post).all().__len__()
    try:
        like = Like.objects.get(post=post,user=request.user)
    except Exception as e:
        like = None
    if like in likes:
        post.is_liked_by_current_user = True
    else:
        post.is_liked_by_current_user = False
    return render(request,'post.html',{'post':post})

def newpost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
        return render(request, "newpost.html",{"form": form})
    form = NewPostForm()
    return render(request, "newpost.html",{"form": form})
