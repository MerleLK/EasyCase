from rest_framework import serializers
from simpleblog import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    # https://github.com/matthewwithanm/django-imagekit/issues/289
    avatar = serializers.ImageField()

    class Meta:
        model = models.User
        fields = '__all__'
