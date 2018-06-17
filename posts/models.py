from django.contrib.auth.models import User
from django.db import models


from categories.models import Categorie



class Post(models.Model):

    # set choices
    PUBLISHED = 'PUB'
    DRAFT = 'DRA'
    STATUSES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft')
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=100)
    post_content = models.TextField()
    image = models.FileField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    img_url = models.CharField(max_length=120)
    categories = models.ManyToManyField(Categorie)
    status = models.CharField(max_length=3, choices=STATUSES, default=DRAFT)

    #return a string representation of any object
    def __str__(self):
        return self.post_title



