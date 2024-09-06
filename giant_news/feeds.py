from django.conf import settings
from django.urls import reverse

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from .models import Article


class RSSFeed(Feed):
    """
    This is a feed of articles, in RSS format.
    """

    def title(self):
        return settings.NEWS_FEED_TITLE or f"Articles from {settings.PRIMARY_HOST}"

    def link(self):
        return reverse("news:rss")

    def description(self):
        return (
            settings.NEWS_FEED_DESCRIPTION
            or f"Latest articles from {settings.PRIMARY_HOST}"
        )

    def items(self):
        return Article.objects.published().order_by("-publish_at")[
            : getattr(settings, "NEWS_FEED_LIMIT", 20)
        ]


class AtomFeed(RSSFeed):
    """
    The same feed of articles, but in Atom format.
    """

    feed_type = Atom1Feed

    def link(self):
        return reverse("news:atom")

    def subtitle(self):
        return self.description()
