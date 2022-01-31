from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from giant_news.models.plugin import RelatedArticlePlugin, RelatedArticleCardPlugin

__all__ = ["RelatedArticlePlugin", "RelatedArticleCardPlugin"]


@plugin_pool.register_plugin
class RelatedArticlePlugin(CMSPluginBase):
    """
    Plugin for the related article model
    """

    model = RelatedArticlePlugin
    name = "Related Articles"
    render_template = "plugins/related_articles/container.html"
    allow_children = True
    child_classes = ["RelatedArticleCardPlugin"]

    def render(self, context, instance, placeholder):
        """
        Override the default render to allow the user to set a custom number of
        articles to be shown
        """
        context = super().render(context, instance, placeholder)
        articles = instance.get_articles()
        current_article = context.get("article")

        if current_article:
            articles.exclude(pk=current_article.pk)

        context.update({"latest_articles": articles[: instance.num_articles]})
        return context


@plugin_pool.register_plugin
class RelatedArticleCardPlugin(CMSPluginBase):
    """
    Plugin for related article card model
    """

    model = RelatedArticleCardPlugin
    name = "Article Cards"
    render_template = "plugins/related_articles/item.html"
    require_parent = True
    parent_class = ["RelatedArticlePlugin"]
