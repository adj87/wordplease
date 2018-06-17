from django import forms

from categories.models import Categorie
from posts.models import Post


class PostForm(forms.ModelForm):

    class Meta:
        # Use model
        model = Post

        # Show fields
        fields = ['post_title', 'post_content', 'image', 'categories']

        # def __init__(self, user, *args, **kwargs):
        #     super(PostForm, self).__init__(*args, **kwargs)
        #     self.fields['categories'].queryset = Categorie.objects.filter(owner=user)

