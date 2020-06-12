from django.views.generic import DetailView, ListView

from .models import Article


class ArticleIndex(ListView):
    """
    Index view for news queryset
    """

    model = Article
    context_object_name = "article_index"
    template_name = "./news_index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        """
        Add published queryset to the context
        """
        context = super().get_context_data(
            object_list=Article.objects.published(), **kwargs
        )
        return context


class ArticleDetail(DetailView):
    """
    Detail view for an news object
    """

    queryset = Article.objects.published()
    template_name = "./news_detail.html"
