import swapper

from django.db import models

from cms.models import CMSPlugin

from giant_news.models import Tag, Category


__all__ = ["RelatedArticlePlugin", "RelatedArticleCardPlugin"]


class RelatedArticlePlugin(CMSPlugin):
    """
    Model for the related article card plugin
    """

    num_articles = models.PositiveIntegerField(
        default=3,
        help_text="""
        This will decide how many articles to return. By
        default this plugin will return this number articles
        based on when they were created. You can filter the
        articles more using the fields below
        """,
    )
    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        help_text="""
        Limit recent articles based on tags. This is the
        first priority in what articles are returned and will be overriden
        if you also select a category.
        """,
    )
    category = models.ForeignKey(
        to=Category,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="""
        Limit recent articles based on a category. This will
        override the tags that you choose and will filter on this category
        ONLY.
        """,
    )

    def __str__(self):
        """
        String representation of the article card object
        """
        return f"Related article block {self.pk}"

    def copy_relations(self, oldinstance):
        """
        Copy tag relations from oldinstance to new
        """
        self.tags.set(oldinstance.tags.all())

    def filter_by_category(self):
        """
        Return a queryset for a category
        """

        return self.recent_articles().filter(category=self.category).distinct()

    def filter_by_tags(self):
        """
        Return a queryset for specified tags
        """
        return self.recent_articles().filter(tags__in=self.tags.all()).distinct()

    def recent_articles(self):
        """
        Return a default queryset
        """
        Article = swapper.load_model("giant_news", "Article")
        return Article.objects.published()

    def get_articles(self):
        """
        Return a queryset based on what the user chooses on the frontend
        """
        queryset = self.recent_articles()

        if self.tags.exists():
            queryset = self.filter_by_tags()
        if self.category:
            queryset = self.filter_by_category()

        return queryset


class RelatedArticleCardPlugin(CMSPlugin):
    """
    A model for an individual article card plugin
    """

    article = models.ForeignKey(
        to=swapper.get_model_name("giant_news", "Article"),
        related_name="related_articles",
        verbose_name="Article",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        """
        String representation of the article card object
        """
        return f"Related article {self.pk}"
