from django import forms
from django.db.models import Q

from giant_news.models import Tag, Category


class NewsSearchForm(forms.Form):
    """
    Form to provide search filtering for articles.
    """

    search = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Search for an article", "title": "Search articles"}
        ),
        required=False,
    )
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(), required=False, widget=forms.CheckboxSelectMultiple(),
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple(),
    )

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop("queryset")
        super().__init__(*args, **kwargs)

    def process(self):
        """
        Filter the queryset based on tags and search query
        """
        search_query = self.cleaned_data.get("search")
        tags = self.cleaned_data.get("tags")
        categories = self.cleaned_data.get("categories")

        if search_query:
            self.queryset = self.queryset.filter(
                Q(title__icontains=search_query)
                | Q(intro__icontains=search_query)
                | Q(plugin_text__icontains=search_query)
            )
        if tags:
            self.queryset = self.queryset.filter(tags__in=tags)

        if categories:
            self.queryset = self.queryset.filter(category__in=categories)

        return self.queryset
