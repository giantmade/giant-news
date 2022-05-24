import swapper

from django.views.generic import DetailView, ListView

from giant_news import forms


Article = swapper.load_model("giant_news", "Article")


class ArticleIndex(ListView):
    """
    Index view for news queryset
    """

    model = Article
    template_name = "news/index.html"
    paginate_by = 8

    def get_queryset(self):
        """
        Override get method here to allow us to filter using tags. This is
        called on get and is the value of self.object_list
        """
        object_list = Article.objects.published(user=self.request.user)
        form = forms.NewsSearchForm(data=self.request.GET or None, queryset=object_list)
        if form.is_valid():
            object_list = form.process()
        return object_list

    def get_context_data(self, **kwargs):
        """
        Update the context with extra args
        """
        context = super().get_context_data(**kwargs)
        context.update({"form": forms.NewsSearchForm(queryset=self.object_list)})
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
            return Article.objects.published(user=self.request.user)
        return self.queryset
