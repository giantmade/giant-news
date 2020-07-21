from django.test import Client
from django.urls import reverse
from django.utils import timezone

import pytest


@pytest.mark.django_db
class TestArticleView:
    """
    Test case for the Article app views
    """

    from news import models

    @pytest.fixture
    def author_instance(self):
        return self.models.Author.objects.create(name="John Doe")

    @pytest.fixture
    def category_instance(self):
        return self.models.Category.objects.create(name="Category")

    @pytest.fixture
    def article_instance(self, author_instance, category_instance):
        return self.models.Article.objects.create(
            title="Article",
            slug="article",
            author=author_instance,
            category=category_instance,
            is_published=True,
            publish_at=timezone.now() - timezone.timedelta(hours=1),
        )

    def test_article_detail(self, article_instance):
        """
        Test the detail view returns the correct status code
        """
        client = Client()

        article = article_instance
        response = client.get(
            reverse("news:news-detail", kwargs={"slug": article.slug})
        )
        assert response.status_code == 200

    def test_article_index(self, article_instance):
        """
        Test the index view returns the correct status code
        """
        client = Client()
        response = client.get(reverse("news:news-index"))
        assert response.status_code == 200

    def test_unpublished_returns_404(
        self, article_instance, author_instance, category_instance
    ):
        """
        Test to check that an unpublished event returns a 404
        """
        client = Client()
        article = self.models.Article.objects.create(
            title="Article Two",
            slug="article-two",
            author=author_instance,
            category=category_instance,
            is_published=False,
            publish_at=timezone.now() - timezone.timedelta(hours=1),
        )

        response = client.get(
            reverse("news:news-detail", kwargs={"slug": article.slug})
        )
        assert response.status_code == 404

    def test_update_context(self, article_instance):
        """
        Test the context update returns published articles queryset
        """
        client = Client()
        article = article_instance
        response = client.get(reverse("news:news-index"))

        assert article in response.context["object_list"]
        assert article in self.models.Article.objects.published()
