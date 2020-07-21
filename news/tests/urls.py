from django.urls import include, path

""""
Url patterns for testing
"""

urlpatterns = [path("news/", include("news.urls", namespace="news"))]
