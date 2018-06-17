from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from blogs.models import Blog


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())



class SignUpForm(UserCreationForm):

    blog_name = forms.CharField(max_length=300)


    class Meta:
        model = User
        fields = ('username', 'blog_name')