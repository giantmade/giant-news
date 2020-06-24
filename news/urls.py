from django.urls import path

from .views import ArticleDetail, ArticleIndex

app_name = "news"

urlpatterns = [
    path("", ArticleIndex.as_view(), name="news-index"),
    path("<slug:slug>/", ArticleDetail.as_view(), name="news-detail"),
]
