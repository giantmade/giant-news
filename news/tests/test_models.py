import pytest


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestArticle:
    # import models here to avoid error
    from news.models import Article, Author

    @pytest.fixture
    def author_instance(self):
        return self.Author.objects.create(first_name="John", last_name="Doe")

    @pytest.fixture
    def article_instance(self, author_instance):
        return self.Article(title="Title", author=author_instance)

    def test_str(self, article_instance):
        assert str(article_instance) == f"Title article by John Doe"


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestArticleTag:
    # import models here to avoid error
    from news.models import ArticleTag

    @pytest.fixture
    def article_tag_instance(self):
        return self.ArticleTag(tag="Tag", slug="tag")

    def test_str(self, article_tag_instance):
        assert str(article_tag_instance) == "Tag"


@pytest.importorskip("django.settings.INSTALLED_APPS")
@pytest.mark.django_db
class TestAuthor:
    # import models here to avoid error
    from news.models import Author

    @pytest.fixture
    def author_instance(self):
        return self.Author(first_name="John", last_name="Doe")

    def test_str(self, author_instance):
        assert str(author_instance) == "John Doe"
