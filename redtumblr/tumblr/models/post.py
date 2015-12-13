from django.db import models

from tumblr.utils.image import *


class PostManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related('blog', )


class Post(models.Model):

    blog = models.ForeignKey('Blog', )

    post_id = models.CharField(
        max_length=65,
    )

    title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='제목',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='요약',
    )
    published_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='발행일',
    )

    original_html = models.TextField(
        blank=True,
        null=True,
        verbose_name='원본 HTML'
    )
    representative_image = models.ImageField(
        upload_to=representative_image_upload_to,
        blank=True,
        null=True,
        verbose_name='대표 이미지',
    )
    screenshot_image = models.ImageField(
        upload_to=screenshot_image_upload_to,
        blank=True,
        null=True,
        verbose_name='스크린샷 이미지',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = PostManager()

    class Meta:
        unique_together = (
            ('blog', 'post_id', ),
        )

    def __str__(self):
        return self.title or self.post_id

    def get_absolute_url(self):
        pass

    def get_original_url(self):
        return self.blog.get_post_url(self.post_id)
