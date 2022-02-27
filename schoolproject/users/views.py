from django.shortcuts import render
from .models import ExtendedUser
from posts.models import Post

def profile(request,id):
    person = ExtendedUser.objects.get(id = id)
    posts = Post.objects.filter(author = person).all()
    return render(request,'profile.html',{ 'user' : person, "posts" : posts })
