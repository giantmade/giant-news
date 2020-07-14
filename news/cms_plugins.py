from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.conf import settings

from . import models

__all__ = ["RelatedArticlePlugin", "RelatedArticleCardPlugin"]


@plugin_pool.register_plugin
class RelatedArticlePlugin(CMSPluginBase):
    """
    Plugin for the related article model
    """

    model = models.RelatedArticlePlugin
    name = "Related Articles"
    render_template = "plugins/related_articles/container.html"
    allow_children = True
    child_classes = ["RelatedArticleCardPlugin"]

    def render(self, context, instance, placeholder):
        """
        Override the default render to allow the user to set a custom number of articles to be shown
        """
        context = super().render(context, instance, placeholder)
        limit = getattr(settings, "RELATED_ARTICLES_LIMIT", 3)
        context["latest_articles"] = instance.get_latest_articles(limit)
        return context


@plugin_pool.register_plugin
class RelatedArticleCardPlugin(CMSPluginBase):
    """
    Plugin for related article card model
    """

    model = models.RelatedArticleCardPlugin
    name = "Article Cards"
    render_template = "plugins/related_articles/item.html"
    require_parent = True
    parent_class = ["RelatedArticlePlugin"]
