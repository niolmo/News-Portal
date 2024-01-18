from django.db import models
from django.db.models.query import QuerySet
from django.utils import timezone
from django.contrib.auth.models import User


class PabMan(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset()\
            .filter(status=Post.Status.PUBLISHED)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name='title')
    slug = models.SlugField(
        max_length=250, verbose_name='URL', unique_for_date='publ')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Автор', verbose_name='author')
    text = models.TextField(verbose_name='text')
    publ = models.DateTimeField(
        verbose_name='Опубликовано', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='updated')
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='status')

    objects = models.Manager()  # Менеджер моделей по умолчанию
    published = PabMan()  # Менеджер моделей опубликованных постов

    class Meta:
        ordering = ['-publ']
        indexes = [
            models.Index(fields=['-publ']),
        ]
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title


class Commetns(models.Model):
    pass
