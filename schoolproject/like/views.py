from django.shortcuts import render, redirect
from posts.models import Post
from .models import Like
from users.models import ExtendedUser

def like_add(request,id,usere):
    posto=Post.objects.get(id = id)
    usero=ExtendedUser.objects.get(id=usere)
    try:
       lik = Like.objects.get(post=posto,user=usero)
       lik.delete()
    except Exception as e:
       like = Like(post=Post.objects.get(id = id),user=ExtendedUser.objects.get(id=usere),like=True)
       like.save()
    referer = request.META.get('HTTP_REFERER')
    return redirect(referer)
