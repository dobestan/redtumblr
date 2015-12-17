from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from tumblr.models import Post


class TumblrPostCachedView(DetailView):
    template_name = 'tumblr/cached/posts/detail.html'
    model = Post
    slug_field = 'post_id'
    context_object_name = 'post'

    def get_queryset(self, *args, **kwargs):
        queryset = super(DetailView, self).get_queryset(*args, **kwargs)

        return queryset.filter(
            blog__slug=self.kwargs.get('blog_slug'),
        )
