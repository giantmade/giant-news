from django.db import models
from django.conf import settings
from django.urls import reverse

from cms.models import PlaceholderField
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

    @property
    def get_absolute_url(self):
        """
        Builds the url for the article object
        """
        url = getattr(settings, "NEWS_ABSOLUTE_URL", "news:news-detail")
        return reverse(url, kwargs={"slug": self.slug})
