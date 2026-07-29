from django.shortcuts import render


def home(request):
    """
    Display the RecipeHub Homepage.
    """
    return render(request, "recipes/home.html")