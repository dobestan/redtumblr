from django.db import models

from tumblr.utils.image import image_image_upload_to


class ImageManager(models.Manager):

    def get_queryset(self):
        return super(models.Manager, self).get_queryset().select_related(
            'post',
            'post__blog',
        )


class Image(models.Model):

    post = models.ForeignKey('Post', )

    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
    )

    original_url = models.URLField(
        verbose_name='원본 이미지 URL',
    )

    image = models.ImageField(
        upload_to=image_image_upload_to,
        blank=True,
        null=True,
        verbose_name='이미지',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = ImageManager()

    class Meta:
        unique_together = (
            ('post', 'original_url', ),
        )

    def __str__(self):
        return self.get_absolute_url()

    def get_absolute_url(self):
        if self.image:
            return self.image.url
        return self.original_url

    def _create_hash_id(self):
        from tumblr.utils.hashids import get_encoded_hashid

        self.hash_id = get_encoded_hashid(self)
        self.save()

    def crawl(self):
        from tumblr.utils.crawler import ImageCrawler

        self.image = ImageCrawler.run(self.original_url)
        self.save()
