from django.contrib.sitemaps import Sitemap

import swapper

Article = swapper.load_model("giant_news", "Article")


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
