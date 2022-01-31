import swapper
from django.db import models

from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.html import strip_tags
from django.test import RequestFactory

from cms.models import PlaceholderField
from cms.plugin_rendering import ContentRenderer
from filer.fields.image import FilerImageField

from mixins.models import PublishingMixin, PublishingQuerySetMixin, TimestampMixin


__all__ = ["Tag", "Author", "Category", "Article", "ArticleQuerySet", "AbstractArticle"]


class Tag(TimestampMixin):
    """
    Model to store a tag for the Article model
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        """
        String representation of the Tag object
        """
        return self.name


class Author(TimestampMixin):
    """
    Model for storing an Author object
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

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


class AbstractArticle(TimestampMixin, PublishingMixin):
    """
    Model for creating and storing and Article object
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(
        to=Author, on_delete=models.CASCADE, related_name="%(app_label)s_articles"
    )
    photo = FilerImageField(
        related_name="%(app_label)s_%(class)s_images",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    intro = models.CharField(max_length=255)
    content = PlaceholderField(
        slotname="article_content", related_name="%(app_label)s_article_content"
    )
    tags = models.ManyToManyField(
        to=Tag, verbose_name="Tags", related_name="%(app_label)s_%(class)s_tags"
    )
    category = models.ForeignKey(
        to=Category, on_delete=models.CASCADE, related_name="%(app_label)s_articles"
    )
    meta_title = models.CharField(max_length=160, blank=True)
    meta_description = models.CharField(max_length=255, blank=True)

    plugin_text = models.TextField(blank=True, editable=False)

    objects = ArticleQuerySet.as_manager()

    class Meta:
        abstract = True
        ordering = ["-publish_at"]

    def __str__(self):
        """
        Returns the string representation of the article object
        """
        return f"{self.title} article by {self.author}"

    def save(self, *args, **kwargs):
        """
        Override save method so we can store the plugin text
        """
        if self.content:
            self.plugin_text = self.plain_text
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """
        Builds the url for the article object
        """
        return reverse("news:detail", kwargs={"slug": self.slug})

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
        if word_count and mins < 1:
            return 1
        return mins


class Article(AbstractArticle):
    """
    Base Article model implementation. Inheriting directly from the
    AbstractArticle class with no further customisation.
    """

    class Meta(AbstractArticle.Meta):
        swappable = swapper.swappable_setting("giant_news", "Article")
        verbose_name = "Article"
        verbose_name_plural = "Articles"
