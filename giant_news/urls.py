from django.urls import path

from .views import ArticleDetail, ArticleIndex

app_name = "giant_news"

urlpatterns = [
    # Index page.
    path("", ArticleIndex.as_view(), name="index"),

    # Feeds.
    path("feed/rss/", ArticleIndex.as_view(), name="rss_feed"),
    path("feed/atom/", ArticleIndex.as_view(), name="atom_feed"),

    # Article detail.
    path("<slug:slug>/", ArticleDetail.as_view(), name="detail"),

]
