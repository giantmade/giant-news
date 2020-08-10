from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.test import RequestFactory

from cms.models import PlaceholderField, CMSPlugin
from cms.plugin_rendering import ContentRenderer
from filer.fields.image import FilerImageField

from mixins.models import PublishingMixin, PublishingQuerySetMixin, TimestampMixin


class ArticleTag(TimestampMixin):
    """
    Model to store a tag for the Article model
    """

    tag = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Article Tag"
        verbose_name_plural = "Article Tags"

    def __str__(self):
        """
        String representation of the Article Tag object
        """
        return self.tag


class Author(TimestampMixin):
    """
    Model for storing an Author object
    """

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name", "-created_at"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        """
        String representation of the Author object
        """
        return self.name


class Category(TimestampMixin):
    """
    Model for creating and storing a Category object
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        """
        String representation of the Category object
        """
        return self.name


class ArticleQuerySet(PublishingQuerySetMixin):
    """
    Custom QuerySet model to override the base one
    """

    pass


class Article(TimestampMixin, PublishingMixin):
    """
    Model for creating and storing and Article object
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, related_name="articles"
    )
    photo = FilerImageField(
        related_name="%(app_label)s_%(class)s_images",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    intro = models.CharField(max_length=255)
    content = PlaceholderField(
        slotname="article_content", related_name="article_content"
    )
    tags = models.ManyToManyField(
        to=ArticleTag, verbose_name="Tags", related_name="%(app_label)s_%(class)s_tags"
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="articles"
    )

    objects = ArticleQuerySet.as_manager()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        """
        Returns the string representation of the article object
        """
        return f"{self.title} article by {self.author}"

    def get_absolute_url(self):
        """
        Builds the url for the article object
        """
        url = getattr(settings, "NEWS_ABSOLUTE_URL", "news:detail")
        return reverse(url, kwargs={"slug": self.slug})

    @cached_property
    def plain_text(self):
        """
        Renders all the plaintext plugins from the placeholder field
        """

        # We need to use this weird ContentRenderer in order to render the plugins
        renderer = ContentRenderer(request=RequestFactory())
        text = ""

        for plugin in self.content.cmsplugin_set.all():
            html = renderer.render_plugin(plugin, {})
            text += strip_tags(html)

        return text.strip()

    @cached_property
    def read_time(self):
        """
        Return estimated article reading time
        """
        word_count = len(self.plain_text.split())
        mins = round(word_count / 240.0)
        if mins < 1:
            return 1
        return mins


class RelatedArticlePlugin(CMSPlugin):
    """
    Model for the related article card plugin
    """

    tags = models.ManyToManyField(
        to=ArticleTag,
        blank=True,
        help_text="Select tags to add the most recent articles.",
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

    def get_latest_articles(self, limit=3):
        """
        Return a specified number of latest articles based on the tags selected
        """
        return (
            Article.objects.published()
            .filter(tags__in=self.tags.all())
            .distinct()
            .order_by("-created_at")[:limit]
        )


class RelatedArticleCardPlugin(CMSPlugin):
    """
    A model for an individual article card plugin
    """

    article = models.ForeignKey(
        to=Article,
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
