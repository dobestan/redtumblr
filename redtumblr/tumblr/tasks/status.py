from celery import Task

from tumblr.models import Blog


class UpdateBlogStatusDetailTask(Task):

    def run(self, blog_id, *args, **kwargs):
        blog = Blog.objects.get(pk=blog_id, )
        blog.update_status()


class UpdateBlogStatusTask(Task):

    def run(self, *args, **kwargs):
        task = UpdateBlogStatusDetailTask()

        for blog in Blog.objects.all():
            task.delay(blog.id)
