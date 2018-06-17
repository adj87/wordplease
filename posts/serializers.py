from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_title', 'image', 'post_content', 'created']


class NewPostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = ['post_title', 'post_content', 'image', 'created', 'categories']


class PostDetailSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'
