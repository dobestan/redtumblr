from django.db import models


class BlogManager(models.Manager):
    pass


class Blog(models.Model):

    slug = models.SlugField(unique=True, )

    title = models.CharField(
        max_length=256,
        blank=True,
        null=True,
        verbose_name='제목',
    )

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    objects = BlogManager()

    class Meta:
        pass

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        pass

    def get_original_url(self):
        return "http://{slug}.tumblr.com/".format(
            slug=self.slug,
        )

    def get_url_with_path(self, path):
        return "{original_url}{path}".format(
            original_url=self.get_original_url(),
            path=path,
        )

    def get_rss_feed_url(self):
        return self.get_url_with_path('rss/')

    def get_archive_url(self):
        return self.get_url_with_path('archive/')

    def get_post_url(self, post_id):
        return self.get_url_with_path(
            "post/{post_id}/".format(
                post_id=post_id,
            )
        )

    def update_posts(self):
        """Update new published posts from RSS Feed."""
        from time import mktime
        from datetime import datetime

        import feedparser

        feed_result = feedparser.parse(self.get_rss_feed_url())

        for item in feed_result.entries:

            original_url = item.id  # http://dobestan.tumblr.com/post/135046057227
            post_id = original_url.split('/')[-1]  # 135046057227

            post, created = self.post_set.get_or_create(
                post_id=post_id,
            )

            if created:
                post.title = item.title or str()

                try:
                    post.description = item.description
                except:
                    pass

                published_parsed = item.published_parsed  # time.struct_time
                post.published_at = datetime.fromtimestamp(mktime(published_parsed))

                post.save()
