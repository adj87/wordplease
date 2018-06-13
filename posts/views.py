from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from posts.models import Post


def posts(request):

    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    return HttpResponse(posts)

def user_posts(request, nombre_de_usuario):

    try:
        posts = Post.objects.filter(owner__username=nombre_de_usuario)
    except Post.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    return HttpResponse(posts)


def post_detail(request, nombre_de_usuario, post_id):

    try:
        post = Post.objects.filter(owner__username=nombre_de_usuario, id=post_id)
    except Post.DoesNotExists:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database',status=404)

    return HttpResponse(post)