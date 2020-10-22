from django.test import Client, RequestFactory
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from news import models, forms, views

import pytest


@pytest.mark.django_db
class TestArticleView:
    """
    Test case for the Article app views
    """

    @pytest.fixture
    def view_instance(self):
        url = reverse("news:index")
        request = RequestFactory().get(url)
        request.user = User(pk=1)
        view = views.ArticleIndex()
        view.kwargs = {}
        view.request = request
        return view

    @pytest.fixture
    def author_instance(self):
        return models.Author.objects.create(name="John Doe")

    @pytest.fixture
    def category_instance(self):
        return models.Category.objects.create(name="Category")

    @pytest.fixture
    def article_instance(self, author_instance, category_instance):
        return models.Article.objects.create(
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
        response = client.get(reverse("news:detail", kwargs={"slug": article.slug}))
        assert response.status_code == 200

    def test_article_index(self, article_instance):
        """
        Test the index view returns the correct status code
        """
        client = Client()
        response = client.get(reverse("news:index"))
        assert response.status_code == 200

    def test_unpublished_returns_404(
        self, article_instance, author_instance, category_instance
    ):
        """
        Test to check that an unpublished article returns a 404
        """
        client = Client()
        article = models.Article.objects.create(
            title="Article Two",
            slug="article-two",
            author=author_instance,
            category=category_instance,
            is_published=False,
            publish_at=timezone.now() - timezone.timedelta(hours=1),
        )

        response = client.get(reverse("news:detail", kwargs={"slug": article.slug}))
        assert response.status_code == 404

    def test_get_queryset(self, mocker, view_instance):
        """
        Test the view get_queryset returns the published qs
        """
        mock_qs = mocker.Mock(return_value="published")
        mocker.patch.object(models.ArticleQuerySet, "published", mock_qs)
        qs = view_instance.get_queryset()

        assert qs == "published"
        mock_qs.assert_called_once_with(user=view_instance.request.user)

    def test_update_context(self, article_instance, view_instance, mocker):
        """
        Test the context update returns published articles queryset and the NewsSearchForm
        """
        mock_qs = mocker.MagicMock(return_value="published")

        view = view_instance
        view.object_list = mock_qs

        context = view.get_context_data()

        assert context["article_index"] is mock_qs
        assert isinstance(context["form"], forms.NewsSearchForm)
