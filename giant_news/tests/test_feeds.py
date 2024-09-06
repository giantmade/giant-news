from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from django.utils.feedgenerator import Atom1Feed

from giant_news import models
from giant_news import feeds


@override_settings(NEWS_FEED_TITLE="Giant News RSS Feed")
@override_settings(NEWS_FEED_DESCRIPTION="Latest articles from Giant News")
class RSSFeedTestCase(TestCase):
    def setUp(self):
        # Setup some content.
        self.category1 = models.Category.objects.create(name="Category")
        self.author1 = models.Author.objects.create(name="John Doe")
        self.article1 = models.Article.objects.create(
            title="Article",
            slug="article",
            author=self.author1,
            category=self.category1,
            is_published=True,
            publish_at=timezone.now() - timezone.timedelta(hours=1),
        )
        self.article2 = models.Article.objects.create(
            title="Another Article",
            slug="another-article",
            author=self.author1,
            category=self.category1,
            is_published=True,
            publish_at=timezone.now() - timezone.timedelta(hours=2),
        )
        self.article3 = models.Article.objects.create(
            title="Unpublished Article",
            slug="unpublished-article",
            author=self.author1,
            category=self.category1,
            is_published=False,
            publish_at=timezone.now() + timezone.timedelta(hours=1),
        )

        # Create the feed
        self.feed = feeds.RSSFeed()

    def test_title(self):
        self.assertEqual(self.feed.title(), "Giant News RSS Feed")

    def test_link(self):
        expected_link = reverse("giant_news:rss")
        self.assertEqual(self.feed.link(), expected_link)

    def test_description(self):
        self.assertEqual(self.feed.description(), "Latest articles from Giant News")

    def test_items(self):
        # Add the articles to the feed
        self.feed.items = lambda: [self.article1, self.article2]

        # Test if the items in the feed match the created articles
        self.assertEqual(list(self.feed.items()), [self.article1, self.article2])
        self.assertNotIn(self.article3, self.feed.items())


@override_settings(NEWS_FEED_TITLE="Giant News Atom Feed")
@override_settings(NEWS_FEED_DESCRIPTION="Latest articles from Giant News")
class AtomFeedTestCase(TestCase):
    def setUp(self):
        self.feed = feeds.AtomFeed()

    def test_feed_type(self):
        self.assertEqual(self.feed.feed_type, Atom1Feed)

    def test_link(self):
        expected_link = reverse("giant_news:atom")
        self.assertEqual(self.feed.link(), expected_link)

    def test_subtitle(self):
        self.assertEqual(self.feed.subtitle(), "Latest articles from Giant News")
