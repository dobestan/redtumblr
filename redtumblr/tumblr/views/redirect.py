from django.views.generic.base import RedirectView
from django.shortcuts import get_object_or_404

from tumblr.models import Blog, Post


class TumblrBlogRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        blog_slug = kwargs.get('blog_slug')

        blog = get_object_or_404(
            Blog,
            slug=blog_slug,
        )

        return blog.get_original_url()


class TumblrPostRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        blog_slug = kwargs.get('blog_slug')
        post_id = kwargs.get('post_id')

        post = get_object_or_404(
            Post,
            blog__slug=blog_slug,
            post_id=post_id,
        )

        return post.get_original_url()
