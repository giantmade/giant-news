from django.contrib import admin

from .models import Article, Tag, Author, Category


READONLY_FIELDS = ["created_at", "updated_at"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    """
    Admin config for the Article model
    """

    list_display = ["title", "author", "category", "is_published", "created_at"]
    search_fields = ["title", "author__name", "intro"]
    prepopulated_fields = {"slug": ["title"]}
    fieldsets = [
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
    ]

    readonly_fields = READONLY_FIELDS


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin config for Tag model
    """

    list_display = ["name", "created_at"]
    fieldsets = [
        (None, {"fields": ["name", "slug"]}),
        ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]}),
    ]
    prepopulated_fields = {"slug": ["name"]}
    readonly_fields = READONLY_FIELDS


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Authors
    """

    list_display = ["name", "created_at"]
    fieldsets = [
        (None, {"fields": ["name", "slug"]}),
        ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]}),
    ]
    prepopulated_fields = {"slug": ["name"]}
    readonly_fields = READONLY_FIELDS


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for editing and creating Category objects
    """

    list_display = ["name", "created_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ["name"]}
    fieldsets = [
        (None, {"fields": ["name", "slug"]}),
        ("Meta Data", {"classes": ("collapse",), "fields": ["created_at", "updated_at"]}),
    ]
    readonly_fields = READONLY_FIELDS
