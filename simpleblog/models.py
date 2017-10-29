from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(
        verbose_name='文章分类',
        max_length=50,
    )


class Tag(models.Model):
    name = models.CharField(
        verbose_name="文章标签",
        max_length=50,
    )


class Post(models.Model):

    title = models.CharField(
        verbose_name='文章标题',
        max_length=50,
    )

    body = models.TextField()

    excerpt = models.CharField(
        verbose_name='文章摘要',
        max_length=200,
        blank=True,
    )

    category = models.ForeignKey(
        Category,
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True,
    )

    author = models.ForeignKey(
        User,
    )

    created_at = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='更新时间',
        auto_now=True,
    )
