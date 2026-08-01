from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Recipe


def home(request):
    """
    Display the homepage with the newest published recipes.
    """

    recent_recipes = (
        Recipe.objects
        .filter(status=Recipe.Status.PUBLISHED)
        .select_related("author", "category")
        .order_by("-created_on")[:3]
    )

    context = {
        "recent_recipes": recent_recipes,
    }

    return render(request, "recipes/home.html", context)


def recipe_list(request):
    """
    Display all published recipes with pagination.
    """

    published_recipes = (
        Recipe.objects
        .filter(status=Recipe.Status.PUBLISHED)
        .select_related("author", "category")
        .order_by("-created_on")
    )

    paginator = Paginator(published_recipes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }

    return render(request, "recipes/recipe_list.html", context)
