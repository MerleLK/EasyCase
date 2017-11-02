from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    r'tags',
    views.TagViewSet,
)
router.register(
    r'categorys',
    views.CategoryViewSet,
)
router.register(
    r'posts',
    views.PostViewSet,
)
router.register(
    r'users',
    views.UserViewSet,
)


urlpatterns = router.urls
