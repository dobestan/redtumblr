from django.core.management.base import BaseCommand

from tumblr.tasks.feed import UpdateBlogFeedTask


class Command(BaseCommand):
    help = "Update Posts from all blogs."

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        task = UpdateBlogFeedTask()
        task.delay()
