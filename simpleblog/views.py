from rest_framework import mixins, generics
from rest_framework.response import Response

from simpleblog import models, serializers


class TagViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
