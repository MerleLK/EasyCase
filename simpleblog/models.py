from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxLengthValidator, RegexValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class BaseModel(models.Model):
    """
    the basic custom's model
    """
    created_at = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='更新时间',
        auto_now=True,
    )

    class Meta:
        abstract = True
        ordering = [
            'created_at',
            'author',
        ]


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(
        max_length=50,
        unique=True,
    )
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        verbose_name='电话',
        max_length=20,
        validators=[
            RegexValidator(r'^[0-9]+$'),
            MaxLengthValidator(11),
        ],
        default='',
        blank=True
    )
    avatar = ProcessedImageField(
        upload_to='avatar',
        default='avatar/default.png',
        verbose_name='头像',
        # 图片将处理成85x85的尺寸
        processors=[ResizeToFill(85, 85)],
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', ]

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.email


class Category(models.Model):
    name = models.CharField(
        verbose_name='文章分类',
        max_length=50,
    )

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        verbose_name="文章标签",
        max_length=50,
    )

    def __str__(self):
        return self.name


class Post(BaseModel):
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
        verbose_name='所属用户',
    )

    def __str__(self):
        return self.title
