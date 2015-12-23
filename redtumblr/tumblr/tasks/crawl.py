from celery import Task

from tumblr.models import Post, Image


class CrawlPostDetailTask(Task):

    def run(self, post_id, *args, **kwargs):
        post = Post.objects.get(pk=post_id, )
        post.crawl_description_images()
        post.crawl()


class CrawlImageDetailTask(Task):

    def run(self, image_id, *args, **kwargs):
        image = Image.objects.get(pk=image_id, )
        image.crawl()
