from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from blogs.models import Blog
from posts.models import Post

def blogs(request):

    try:
        blogs = Blog.objects.all()
    except Blog.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    return HttpResponse(blogs)


