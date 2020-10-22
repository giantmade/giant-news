from django import forms
from django.db.models import Q

from news.models import ArticleTag


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
    tags = forms.ModelMultipleChoiceField(
        queryset=ArticleTag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
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

        if search_query:
            self.queryset = self.queryset.filter(
                Q(title__icontains=search_query) | Q(intro__icontains=search_query)
            )
        if tags:
            self.queryset = self.queryset.filter(tags__in=tags)

        return self.queryset
