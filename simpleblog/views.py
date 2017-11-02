from rest_framework import mixins, viewsets

from simpleblog import models, serializers


class TagViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class UserViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
