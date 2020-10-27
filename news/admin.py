from django.conf import settings
from django.contrib import admin

from .models import Article, ArticleTag, Author, Category


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    """
    Admin config for ArticleTag model
    """

    list_display = getattr(
        settings, "ARTICLETAG_ADMIN_LIST_DISPLAY", ["tag", "created_at"]
    )

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
        settings,
        "ARTICLE_ADMIN_LIST_DISPLAY",
        ["title", "author", "category", "is_published", "created_at"],
    )
    search_fields = getattr(
        settings, "ARTICLE_ADMIN_SEARCH_FIELDS", ["title", "author__name", "intro"]
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
                        "category",
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
        settings, "AUTHOR_ADMIN_LIST_DISPLAY", ["name", "created_at"]
    )
    fieldsets = getattr(
        settings,
        "AUTHOR_ADMIN_FIELDSETS",
        [
            ("Details", {"fields": ["name"]},),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )

    readonly_fields = getattr(
        settings, "AUTHOR_ADMIN_READONLY_FIELDS", ["created_at", "updated_at"],
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Category objects
    """

    list_display = getattr(
        settings, "CATEGORY_ADMIN_LIST_DISPLAY", ["name", "created_at"]
    )
    search_fields = getattr(settings, "CATEGORY_ADMIN_SEARCH_FIELDS", ["name"])
    prepopulated_fields = {"slug": ["name"]}
    fieldsets = getattr(
        settings,
        "CATEGORY_ADMIN_FIELDSETS",
        [
            (None, {"fields": ["name", "slug"]}),
            (
                "Meta Data",
                {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},
            ),
        ],
    )
