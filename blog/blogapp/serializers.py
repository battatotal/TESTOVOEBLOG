from rest_framework import serializers
from django.contrib.auth.models import User

from blogapp.models import Post

#Сериализатор для данных из модели User
class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


#Сериализатор для данных из модели Post
class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"