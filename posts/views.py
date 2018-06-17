from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View

from posts.forms import PostForm
from posts.models import Post
from project.settings import BASE_DIR


def posts(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    context = {
        'posts': posts
    }

    return render(request, 'posts_list.html', context)


def user_posts(request, nombre_de_usuario):
    try:
        posts = Post.objects.filter(owner__username=nombre_de_usuario)
    except Post.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    context = {
        'posts': posts,
    }
    return render(request, 'posts_list.html', context)
    # return HttpResponse(BASE_DIR+'ui')


class PostDetail(View):

    def get(self, request, nombre_de_usuario, post_id):

        try:
            post = Post.objects.get(owner__username=nombre_de_usuario, pk=post_id)
        except Post.DoesNotExist:
            # If post does not exist, return 404
            return HttpResponse('Post doesn´t exist in database', status=404)


        context = {
            'post': post,
        }

        return render(request, 'post_detail.html', context)


@method_decorator(login_required, name='dispatch')
class NewPostView(View):

    """
    New post view class
    """

    def get(self, request):

        form = PostForm()

        context = {'form': form}
        return render(request, 'post_new.html', context)

    def post(self, request):
        # Define new instance
        post = Post()

        # Add user logged
        post.owner = request.user

        # Create form
        form = PostForm(request.POST, request.FILES, instance=post)

        # Validate form
        if form.is_valid():
            # Create add
            post = form.save()

        return redirect('blogs')