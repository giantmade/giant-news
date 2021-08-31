from django.conf import settings
from django.views.generic import DetailView, ListView

from . import models, forms


class ArticleIndex(ListView):
    """
    Index view for news queryset
    """

    model = models.Article
    context_object_name = "article_index"
    template_name = "news/index.html"
    paginate_by = getattr(settings, "NEWS_PAGINATE_BY", 8)

    def get_queryset(self):
        """
        Override get method here to allow us to filter using tags
        """
        queryset = models.Article.objects.published(user=self.request.user)
        form = forms.NewsSearchForm(data=self.request.GET or None, queryset=queryset)
        if form.is_valid():
            queryset = form.process()
        return queryset

    def get_context_data(self, **kwargs):
        """
        Update the context with extra args
        """
        context = super().get_context_data(**kwargs)
        context["form"] = forms.NewsSearchForm(queryset=self.object_list)
        context["article_index"] = self.object_list
        return context


class ArticleDetail(DetailView):
    """
    Detail view for an news object
    """

    template_name = "news/detail.html"

    def get_queryset(self):
        """
        Override the default queryset method so that we can access the request.user
        """
        if self.queryset is None:
            return models.Article.objects.published(user=self.request.user)
        return self.queryset
