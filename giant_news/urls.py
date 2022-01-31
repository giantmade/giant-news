from django.urls import path

from .views import ArticleDetail, ArticleIndex

app_name = "giant_news"

urlpatterns = [
    path("", ArticleIndex.as_view(), name="index"),
    path("<slug:slug>/", ArticleDetail.as_view(), name="detail"),
]
