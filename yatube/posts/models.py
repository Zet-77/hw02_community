from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        verbose_name='Информация о группах',
        max_length=200
    )
    slug = models.SlugField(
        max_length=200, unique=True,
        db_index=True, verbose_name='slug'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    related_name = ('group')

    class Meta:
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        max_length=30, verbose_name='Текст'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name=('posts'),
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group, blank=True, null=True,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'posts'


