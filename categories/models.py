from django.db import models


# Create your models here.

class Categorie(models.Model):
    categorie_name = models.CharField(max_length=30)
    creation_date = models.DateTimeField(auto_now_add=True)
