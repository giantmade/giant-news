from django.conf import settings

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class NewsApp(CMSApp):
    """
    App hook for News app
    """

    app_name = "news"
    name = "News"

    def get_urls(self, page=None, language=None, **kwargs):
        """
        Return the path to the apps urls module
        """

        return ["giant_news.urls"]


if settings.REGISTER_NEWS_APP:
    apphook_pool.register(NewsApp)
