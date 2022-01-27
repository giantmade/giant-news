from django.urls import include, path

""""
Url patterns for testing
"""

urlpatterns = [path("news/", include("giant_news.urls", namespace="news"))]
