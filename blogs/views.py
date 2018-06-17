from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login, logout as django_logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
# Create your views here.
from django.views import View

from blogs.forms import LoginForm, SignUpForm
from blogs.models import Blog
from posts.models import Post


def blogs(request):

    try:
        blogs = Blog.objects.all()
    except Blog.DoesNotExist:
        # If ad don't exist return 404
        return HttpResponse('Post doesn´t exist in database', status=404)

    context = {'blogs': blogs}
    return render(request, 'blogs.html', context)


class LoginView(View):

    def get(self, request):
        """
        Muestra el formulario de login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        """
        Procesa el login de un usuario
        :param request: objeto HttpRequest
        :return: objeto HttpResponse con el formulario renderizado
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # comprobamos si las credenciales son correctas
            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, 'Usuario o contraseña incorrecto')
            else:
                # iniciamos la sesión del usuario (hacemos login del usuario)
                django_login(request, user)
                url = request.GET.get('next', 'home')
                return redirect(url)

        context = {'form': form}
        return render(request, 'login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace logout de un usuario y le redirige al login
        :param request: objeto HttpRequest
        :return: objeto HttpResponse de redirección al login
        """
        django_logout(request)
        return redirect('login')


def signupview(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.blog.blog_name = form.cleaned_data.get('blog_name')
            user.blog.blog_description = form.cleaned_data.get('blog_description')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            django_login(request, user)

            # Get next url parameter
            url = request.GET.get('next', 'home')

            # Redirect user
            return redirect(url)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})