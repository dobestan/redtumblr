from django.views.generic.base import RedirectView


class FacebookPageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        facebook_page_id = '307717916235360'
        return "https://www.facebook.com/{facebook_page_id}/".format(
            facebook_page_id=facebook_page_id,
        )


class FacebookMessageRedirectView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        facebook_page_id = '307717916235360'
        return "https://m.facebook.com/messages/thread/{facebook_page_id}".format(
            facebook_page_id=facebook_page_id,
        )
