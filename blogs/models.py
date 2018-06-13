from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    blog_name = models.CharField(max_length=30)
