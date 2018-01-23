import re

from rest_framework import routers, viewsets


def underscore(string, spliter='_'):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1%s\2' % spliter, string)
    return re.sub('([a-z0-9])([A-Z])', r'\1%s\2' % spliter, s1).lower()


class MyDefaultRouter(routers.SimpleRouter):
    routes = [
        routers.SimpleRouter.routes[0],  # list route
        routers.DynamicListRoute(
            url=r'^{prefix}/{methodnamehyphen}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
        routers.SimpleRouter.routes[2],  # detail route
        routers.DynamicDetailRoute(
            url=r'^{prefix}/{lookup}/{methodnamehyphen}{trailing_slash}$',
            name='{basename}-{methodnamehyphen}',
            initkwargs={}
        ),
    ]
    VIEWSET_NAME_REGEXP = re.compile(r'(?P<name>\w+)ViewSet')

    def __init__(self):
        super(MyDefaultRouter, self).__init__(trailing_slash=False)

    def register(self, viewset, prefix=None, base_name=None):
        assert issubclass(viewset, viewsets.ViewSetMixin), "first argument must be a viewset"

        match = self.VIEWSET_NAME_REGEXP.fullmatch(viewset.__name__)

        assert match is not None, "viewset class name '%s' not match '%s'" % (
            viewset.__name__,
            self.VIEWSET_NAME_REGEXP.pattern
        )
        name = underscore(match.group('name'), spliter='-')

        if prefix is None:
            prefix = name + 's'

        if base_name is None:
            base_name = name

        return super(MyDefaultRouter, self).register(
            prefix=prefix,
            viewset=viewset,
            base_name=base_name,
        )
