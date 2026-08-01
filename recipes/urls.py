from django.urls import path

from . import views


app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path(
        "recipes/<slug:slug>/",
        views.recipe_detail,
        name="recipe_detail",
    ),
]
