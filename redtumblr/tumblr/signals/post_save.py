from django.db.models.signals import post_save
from django.dispatch import receiver

from tumblr.models import Blog, Post, Image
from tumblr.tasks.feed import UpdateBlogFeedDetailTask
from tumblr.tasks.status import UpdateBlogStatusDetailTask
from tumblr.tasks.crawl import CrawlPostDetailTask, CrawlImageDetailTask


@receiver(post_save, sender=Blog)
def post_save_blog(sender, instance, created, **kwargs):
    import feedparser

    if created:
        # Update Blog title
        feed_result = feedparser.parse(instance.get_rss_feed_url())
        instance.title = feed_result.feed.title
        instance.save()

        # Update Blog posts
        feed_task = UpdateBlogFeedDetailTask()
        feed_task.delay(instance.id)


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):

    if created:
        task = CrawlPostDetailTask()
        task.delay(instance.id)


@receiver(post_save, sender=Image)
def post_save_image(sender, instance, created, **kwargs):

    if created:
        instance._create_hash_id()

        task = CrawlImageDetailTask()
        task.delay(instance.id)
