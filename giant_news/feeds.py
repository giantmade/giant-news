from django.conf import settings
from django.urls import reverse

from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed

from .models import Article

class RSSFeed(Feed):
    description = "Updates on changes and additions to police beat central."

    def title(self):
        return settings.NEWS_FEED_TITLE or "Articles"

    def link(self):
        return reverse("news:index") 
    
    def description(self):
        return settings.NEWS_FEED_DESCRIPTION or f"Latest articles from {settings.PRIMARY_HOST}"

    def items(self):
        return Article.objects.published()[:20]


class AtomFeed(RSSFeed):
    feed_type = Atom1Feed
    subtitle = RSSFeed.description
