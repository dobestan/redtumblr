from django.apps import AppConfig


class TumblrAppConfig(AppConfig):
    name = 'tumblr'

    def ready(self):
        from tumblr.signals.post_save import post_save_blog, post_save_post
