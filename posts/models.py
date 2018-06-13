from django.contrib.auth.models import User
from django.db import models


from categories.models import Categorie


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    image = models.FileField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    img_url = models.CharField(max_length=120)
    categories = models.ManyToManyField(Categorie)