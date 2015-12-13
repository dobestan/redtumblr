from celery import Task

from tumblr.models import Blog


class UpdateBlogFeedDetailTask(Task):

    def run(self, blog_id, *args, **kwargs):
        blog = Blog.objects.get(pk=blog_id, )
        blog.update_posts()


class UpdateBlogFeedTask(Task):

    def run(self, *args, **kwargs):
        task = UpdateBlogFeedDetailTask()

        for blog in Blog.objects.all():
            task.delay(blog.id)
