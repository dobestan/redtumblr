from celery import Task

from tumblr.models import Post


class CrawlPostDetailTask(Task):

    def run(self, post_id, *args, **kwargs):
        post = Post.objects.get(pk=post_id, )
        post.crawl()
