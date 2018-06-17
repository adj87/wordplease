"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blogs.api import UsersApi, UserDetailAPI, BlogsApi
from blogs.views import blogs, LoginView, LogoutView, signupview
from posts.api import PostListAPI, PostDetailAPI, UserPostListAPI
from posts.views import posts, user_posts, NewPostView, PostDetail

urlpatterns = [
    path('', posts, name='home'),
    path('admin/', admin.site.urls),
    path('blogs/', blogs, name='blogs'),
    path('blogs/<str:nombre_de_usuario>/', user_posts, name='user_posts_list'),
    path('blogs/<str:nombre_de_usuario>/<int:post_id>/', PostDetail.as_view(), name='post_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', signupview, name='signup'),
    path('new-post/', NewPostView.as_view(), name='new-post'),

    #API URLS
    path('api/v1/users/', UsersApi.as_view(), name='apiv1-users'),
    path('api/v1/users/<int:pk>/', UserDetailAPI.as_view(), name='apiv1-user-detail'),
    path('api/v1/blogs/', BlogsApi.as_view(), name='apiv1-blogs'),
    path('api/v1/posts/', PostListAPI.as_view(), name='apiv1-posts'),
    path('api/v1/posts/<int:pk>/', PostDetailAPI.as_view(), name='apiv1-post-detail'),
    path('api/v1/posts/mine/', UserPostListAPI.as_view(), name='apiv1-user-mine'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
