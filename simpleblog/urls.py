from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from utils.router_utils import MyDefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)

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

sim_router = MyDefaultRouter()
sim_router.register(
    views.TagViewSet,
)


urlpatterns = router.urls
