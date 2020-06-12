from django.conf import settings
from django.contrib import admin

from .models import Article, ArticleTag, Author


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    """
    Admin config for ArticleTag model
    """

    list_display = getattr(settings, "ARTICLETAG_ADMIN_LIST_DISPLAY", ["tag"])

    fieldsets = getattr(
        settings,
        "ARTICLETAG_ADMIN_FIELDSETS",
        [
            (None, {"fields": ["tag", "slug"]}),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )
    readonly_fields = getattr(
        settings, "ARTICLETAG_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"],
    )
    prepopulated_fields = {"slug": ["tag"]}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin config for the Article model
    """

    list_display = getattr(
        settings, "ARTICLE_ADMIN_LIST_DISPLAY", ["title", "author", "is_published"]
    )
    search_fields = getattr(
        settings, "ARTICLE_ADMIN_SEARCH_FIELDS", ["title", "author"]
    )
    prepopulated_fields = {"slug": ["title"]}

    fieldsets = getattr(
        settings,
        "ARTICLE_ADMIN_FIELDSETS",
        [
            (
                "Details",
                {
                    "fields": [
                        "title",
                        "slug",
                        "author",
                        "intro",
                        "tags",
                        "is_published",
                        "publish_at",
                    ]
                },
            ),
            ("Image", {"fields": ["photo"]}),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )

    readonly_fields = getattr(
        settings, "ARTICLE_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"],
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Authors
    """

    list_display = getattr(
        settings, "AUTHOR_ADMIN_LIST_DISPLAY", ["first_name", "last_name"]
    )
    fieldsets = getattr(
        settings,
        "AUTHOR_ADMIN_FIELDSETS",
        [
            ("Details", {"fields": ["first_name", "last_name"]},),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )

    readonly_fields = getattr(
        settings, "AUTHOR_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"],
    )
