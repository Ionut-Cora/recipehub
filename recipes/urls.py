from django.urls import path

from . import views


app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard",
    ),
    path(
        "recipes/", 
        views.recipe_list, 
        name="recipe_list"
    ),
    path(
        "recipes/create/",
        views.recipe_create,
        name="recipe_create",
    ),
    path(
        "recipes/<slug:slug>/edit/",
        views.recipe_edit,
        name="recipe_edit",
    ),
    path(
        "recipes/<slug:slug>/delete/",
        views.recipe_delete,
        name="recipe_delete",
    ),
    path(
        "recipes/<slug:slug>/comment/",
        views.comment_create,
        name="comment_create",
    ),

    path(
        "comments/<int:comment_id>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path(
        "recipes/<slug:slug>/",
        views.recipe_detail,
        name="recipe_detail",
    ),
]
