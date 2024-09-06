from django.urls import path
from django.conf import settings

from .views import ArticleDetail, ArticleIndex

app_name = "giant_news"

urlpatterns = [
    # Index page.
    path("", ArticleIndex.as_view(), name="index"),

    # Article detail.
    path("<slug:slug>/", ArticleDetail.as_view(), name="detail"),

]

if getattr(settings, "NEWS_FEEDS_ENABLED", True):
    from .feeds import RSSFeed, AtomFeed

    urlpatterns = [
        path("rss/", RSSFeed(), name="rss"),
        path("atom/", AtomFeed(), name="atom"),
    ] + urlpatterns