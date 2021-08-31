import pytest
from django.db.models import Q
from news import forms


@pytest.mark.django_db
class TestNewsFilterForm:
    @pytest.fixture
    def form(self, mocker):
        return forms.NewsSearchForm(queryset=mocker.Mock())

    def test_filter_by_search_term(self, mocker, form):
        articles = form.queryset
        articles.filter.return_value = "qs"
        clean_data = {
            "search": "great",
        }
        form.cleaned_data = clean_data
        result = form.process()

        assert result == "qs"
        articles.filter.assert_called_once_with(
            Q(title__icontains="great") | Q(intro__icontains="great") | Q(plugin_text__icontains="great")
        )

    def test_filter_by_search_no_data(self, mocker, form):
        articles = form.queryset
        form.cleaned_data = {}
        result = form.process()

        assert result == articles
        articles.filter.assert_not_called()

    def test_filter_by_tags(self, mocker, form):
        articles = form.queryset
        articles.filter.return_value = "qs"
        clean_data = {
            "tags": "running",
        }
        form.cleaned_data = clean_data
        result = form.process()

        assert result == "qs"
        articles.filter.assert_called_once_with(tags__in="running")

    def test_filter_by_tags_no_data(self, mocker, form):
        articles = form.queryset
        form.cleaned_data = {}
        result = form.process()

        assert result == articles
        articles.filter.assert_not_called()

    def test_filter_by_category(self, mocker, form):
        articles = form.queryset
        articles.filter.return_value = "qs"
        clean_data = {
            "categories": "blog",
        }
        form.cleaned_data = clean_data
        result = form.process()

        assert result == "qs"
        articles.filter.assert_called_once_with(category__in="blog")

    def test_filter_by_category_no_data(self, mocker, form):
        articles = form.queryset
        form.cleaned_data = {}
        result = form.process()

        assert result == articles
        articles.filter.assert_not_called()
