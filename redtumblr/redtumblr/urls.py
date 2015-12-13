from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from redtumblr.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include([
        url(r'^facebook/$', FacebookPageRedirectView.as_view(), name='page'),
        url(r'^facebook/message/$', FacebookMessageRedirectView.as_view(), name='message'),

        url(r'^contact/$', FacebookMessageRedirectView.as_view(), name='contact'),
    ], namespace='facebook')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
