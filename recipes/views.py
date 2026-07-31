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
