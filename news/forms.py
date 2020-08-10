from django import forms

from news.models import ArticleTag, Article


class NewsSearchForm(forms.Form):
    """
    Form to provide search filtering for events.
    """

    tags = forms.ModelMultipleChoiceField(
        queryset=ArticleTag.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
    )

    def __init__(self, *args, **kwargs):
        self.queryset = kwargs.pop("queryset")

    def process(self):
        """
        Additionally apply tags filter to the results.
        """
        tags = self.cleaned_data.get("tags")
        return self.queryset.filter(tags__in=tags)
