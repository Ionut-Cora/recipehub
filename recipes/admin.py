from django.contrib import admin

from .models import Category, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for recipe categories.
    """

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Admin configuration for recipes.
    """

    list_display = (
        "title",
        "author",
        "category",
        "status",
        "difficulty",
        "created_on",
    )

    list_filter = (
        "status",
        "difficulty",
        "category",
        "created_on",
    )

    search_fields = (
        "title",
        "summary",
        "author__username",
    )

    prepopulated_fields = {
        "slug": ("title",),
    }

    readonly_fields = (
        "created_on",
        "updated_on",
    )

    ordering = (
        "-created_on",
    )
