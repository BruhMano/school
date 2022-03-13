from django.shortcuts import render
from .models import ExtendedUser
from posts.models import Post
from like.models import Like

def profile(request,id):
    likes = Like.objects.all()
    person = ExtendedUser.objects.get(id = id)
    posts = Post.objects.filter(author = person).all()
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
    return render(request,'profile.html',{ 'user' : person, "posts" : posts })
