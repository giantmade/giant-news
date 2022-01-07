from django.conf import settings
from django.contrib import admin

from .models import Article, ArticleTag, Author, Category


READONLY_FIELDS = ["created_at", "updated_at"]


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
                {
                    "classes": ("collapse",),
                    "fields": ["meta_title", "meta_description", "created_at", "updated_at"],
                },
            ),
        ],
    )

    readonly_fields = getattr(
        settings, "ARTICLE_ADMIN_READONLY_FIELDS", READONLY_FIELDS,
    )


@admin.register(ArticleTag)
class ArticleTagAdmin(admin.ModelAdmin):
    """
    Admin config for ArticleTag model
    """

    list_display = ["tag", "created_at"]
    fieldsets = (
        [
            (None, {"fields": ["tag", "slug"]}),
            ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},),
        ],
    )
    prepopulated_fields = {"slug": ["tag"]}
    readonly_fields = READONLY_FIELDS


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Authors
    """

    list_display = ["name", "created_at"]
    fieldsets = (
        [
            ("Details", {"fields": ["name"]},),
            ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},),
        ],
    )
    readonly_fields = READONLY_FIELDS


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Category objects
    """

    list_display = "name", "created_at"
    search_fields = "name"
    prepopulated_fields = {"slug": ["name"]}
    fieldsets = (
        [
            (None, {"fields": ["name", "slug"]}),
            ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]},),
        ],
    )
    readonly_fields = READONLY_FIELDS
