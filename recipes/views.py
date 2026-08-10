from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Comment, Recipe
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CommentForm, RecipeForm
from django.db.models import Q


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
    Display published recipes with search, category filtering,
    and pagination.
    """

    published_recipes = (
        Recipe.objects
        .filter(status=Recipe.Status.PUBLISHED)
        .select_related("author", "category")
        .prefetch_related("recipe_ingredients__ingredient")
        .order_by("-created_on")
    )

    search_query = request.GET.get("q", "").strip()
    category_id = request.GET.get("category", "").strip()

    if search_query:
        published_recipes = published_recipes.filter(
            Q(title__icontains=search_query)
            | Q(
                recipe_ingredients__ingredient__name__icontains=
                search_query
            )
        ).distinct()

    if category_id:
        published_recipes = published_recipes.filter(
            category_id=category_id
        )

    paginator = Paginator(published_recipes, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        "page_obj": page_obj,
        "categories": categories,
        "search_query": search_query,
        "selected_category": category_id,
    }

    return render(
        request,
        "recipes/recipe_list.html",
        context,
    )


def recipe_detail(request, slug):
    """
    Display a published recipe and its comments.
    """

    recipe = get_object_or_404(
        Recipe.objects
        .select_related("author", "category")
        .prefetch_related(
            "recipe_ingredients__ingredient",
            "comments__author",
        ),
        slug=slug,
        status=Recipe.Status.PUBLISHED,
    )

    comments = recipe.comments.select_related(
        "author"
    ).all()

    comment_form = CommentForm()

    context = {
        "recipe": recipe,
        "comments": comments,
        "comment_form": comment_form,
    }

    return render(
        request,
        "recipes/recipe_detail.html",
        context,
    )


@login_required
def recipe_create(request):
    """
    Allow an authenticated user to create a new recipe.
    """

    if request.method == "POST":
        form = RecipeForm(
            request.POST,
            request.FILES,
        )

        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            messages.success(
                request,
                "Your recipe has been created successfully.",
            )

            return redirect(
                "recipes:recipe_detail",
                slug=recipe.slug,
            )
    else:
        form = RecipeForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "recipes/recipe_form.html",
        context,
    )


@login_required
def recipe_edit(request, slug):
    """
    Allow the recipe author to edit their own recipe.
    """

    recipe = get_object_or_404(
        Recipe,
        slug=slug,
        author=request.user,
    )

    if request.method == "POST":
        form = RecipeForm(
            request.POST,
            request.FILES,
            instance=recipe,
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your recipe has been updated successfully.",
            )

            return redirect(
                "recipes:recipe_detail",
                slug=recipe.slug,
            )
    else:
        form = RecipeForm(instance=recipe)

    context = {
        "form": form,
        "recipe": recipe,
        "is_editing": True,
    }

    return render(
        request,
        "recipes/recipe_form.html",
        context,
    )


@login_required
def recipe_delete(request, slug):
    """
    Allow the recipe author to delete their own recipe.
    """

    recipe = get_object_or_404(
        Recipe,
        slug=slug,
        author=request.user,
    )

    if request.method == "POST":
        recipe.delete()

        messages.success(
            request,
            "Your recipe has been deleted successfully.",
        )

        return redirect("recipes:recipe_list")

    context = {
        "recipe": recipe,
    }

    return render(
        request,
        "recipes/recipe_confirm_delete.html",
        context,
    )


@login_required
def comment_create(request, slug):
    """
    Allow an authenticated user to comment on a published recipe.
    """

    recipe = get_object_or_404(
        Recipe,
        slug=slug,
        status=Recipe.Status.PUBLISHED,
    )

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.author = request.user
            comment.save()

            messages.success(
                request,
                "Your comment has been added.",
            )

    return redirect(
        "recipes:recipe_detail",
        slug=recipe.slug,
    )


@login_required
def comment_delete(request, comment_id):
    """
    Allow a user to delete their own comment.
    """

    comment = get_object_or_404(
        Comment,
        id=comment_id,
        author=request.user,
    )

    recipe_slug = comment.recipe.slug

    if request.method == "POST":
        comment.delete()

        messages.success(
            request,
            "Your comment has been deleted.",
        )

    return redirect(
        "recipes:recipe_detail",
        slug=recipe_slug,
    )
