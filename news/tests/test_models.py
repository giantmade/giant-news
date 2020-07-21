import pytest


@pytest.mark.django_db
class TestArticle:
    # import models here to avoid error
    from news.models import Article, Author

    @pytest.fixture
    def author_instance(self):
        return self.Author.objects.create(name="John Doe")

    @pytest.fixture
    def article_instance(self, author_instance):
        return self.Article(title="Title", author=author_instance)

    def test_str(self, article_instance):
        assert str(article_instance) == f"Title article by John Doe"


class TestArticleTag:
    # import models here to avoid error
    from news.models import ArticleTag

    @pytest.fixture
    def article_tag_instance(self):
        return self.ArticleTag(tag="Tag")

    def test_str(self, article_tag_instance):
        assert str(article_tag_instance) == "Tag"


class TestAuthor:
    # import models here to avoid error
    from news.models import Author

    @pytest.fixture
    def author_instance(self):
        return self.Author(name="John Doe")

    def test_str(self, author_instance):
        assert str(author_instance) == "John Doe"


class TestCategory:
    # import models here to avoid error
    from news.models import Category

    @pytest.fixture
    def category_instance(self):
        return self.Category(name="Category")

    def test_str(self, category_instance):
        assert str(category_instance) == "Category"
