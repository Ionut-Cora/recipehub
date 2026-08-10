from django.contrib import admin

from .models import Category, Comment, Ingredient, Recipe, RecipeIngredient


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for recipe categories.
    """

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Admin configuration for reusable ingredients.
    """

    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


class RecipeIngredientInline(admin.TabularInline):
    """
    Allow ingredients to be managed from the recipe admin page.
    """

    model = RecipeIngredient
    extra = 1
    autocomplete_fields = ("ingredient",)


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

    inlines = [
        RecipeIngredientInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for recipe comments.
    """

    list_display = (
        "author",
        "recipe",
        "created_on",
    )

    list_filter = (
        "created_on",
    )

    search_fields = (
        "author__username",
        "recipe__title",
        "body",
    )

    ordering = (
        "-created_on",
    )
