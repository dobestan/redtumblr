from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from redtumblr.views import *
from tumblr.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^facebook/$', FacebookPageRedirectView.as_view(), name='page'),
        url(r'^facebook/message/$', FacebookMessageRedirectView.as_view(), name='message'),
        url(r'^contact/$', FacebookMessageRedirectView.as_view(), name='contact'),
    ], namespace='facebook')),

    url(r'^r/', include([
        url(r'^(?P<blog_slug>\w+)/$', TumblrBlogRedirectView.as_view(), name='blog'),
        url(r'^(?P<blog_slug>\w+)/(?P<post_id>\w+)/$', TumblrPostRedirectView.as_view(), name='post'),
    ], namespace='redirect')),

    url(r'^c/', include([
        url(r'^(?P<blog_slug>\w+)/(?P<slug>\w+)/$', TumblrPostCachedView.as_view(), name='post'),
    ], namespace='cached')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
