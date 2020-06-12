from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register
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

        return ["news.urls"]
