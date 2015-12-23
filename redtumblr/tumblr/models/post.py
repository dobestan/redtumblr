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
    representative_image_url = models.URLField(
        blank=True,
        null=True,
        verbose_name='대표 이미지 URL',
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

    def create_image(self, original_url):
        if 'default' not in original_url and\
                'assets.tumblr.com' not in original_url:
            self.image_set.create(
                original_url=original_url,
            )

    def crawl_description_images(self):
        import lxml.html

        dom = lxml.html.fromstring(self.description)

        image_elements = dom.cssselect('img')
        if image_elements:
            for image_element in image_elements:
                original_url = image_element.get('src')
                self.create_image(original_url)

        video_elements = dom.cssselect('video')
        if video_elements:
            for video_element in video_elements:
                original_url = video_element.get('poster')
                self.create_image(original_url)

    def crawl(self):
        from django.core.files import File
        from django.core.files.temp import NamedTemporaryFile

        from selenium import webdriver

        driver = webdriver.PhantomJS()
        driver.get(self.get_original_url())

        self.original_html = driver.page_source

        # Save a post screenshot.
        try:
            image_file_png_binary = driver.get_screenshot_as_png()

            image_file_temp = NamedTemporaryFile(delete=True)
            image_file_temp.write(image_file_png_binary)
            image_file_temp.flush()

            image = File(image_file_temp)
            image.name = "{filename}.png".format(
                filename=self.post_id,
            )
        except:
            image = None

        self.screenshot_image = image
        self.save()

        # Save images as Image instance.
        try:
            iframe_url = driver.find_element_by_css_selector('section#posts.content iframe').get_attribute('src')
            driver.get(iframe_url)

            image_elements = driver.find_elements_by_css_selector('img')
            if image_elements:
                for image_element in image_elements:
                    original_url = image_element.get_attribute('src')
                    self.image_set.create(
                        original_url=original_url,
                    )
        except:
            pass
