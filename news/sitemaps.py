from django.contrib.sitemaps import Sitemap

from .models import Article


class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        """
        Get all published articles
        """
        return Article.objects.published()

    def lastmod(self, obj):
        return obj.updated_at
