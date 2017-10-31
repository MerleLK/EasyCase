# from django.contrib import admin
import xadmin
from simpleblog.models import Category, Tag, Post

xadmin.site.register(Category)
xadmin.site.register(Tag)
xadmin.site.register(Post)
