from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """
    Represents a category used to organise recipes.
    """

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Represents a recipe created by a registered RecipeHub user.
    """

    class Difficulty(models.TextChoices):
        EASY = "easy", "Easy"
        MEDIUM = "medium", "Medium"
        HARD = "hard", "Hard"

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipes",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="recipes",
    )

    title = models.CharField(
        max_length=200,
        unique=True,
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True,
    )

    summary = models.TextField(
        max_length=500,
        help_text="Provide a short description of the recipe.",
    )

    instructions = models.TextField(
        help_text="Explain how to prepare the recipe.",
    )

    preparation_time = models.PositiveIntegerField(
        help_text="Preparation time in minutes.",
    )

    cooking_time = models.PositiveIntegerField(
        help_text="Cooking time in minutes.",
    )

    servings = models.PositiveIntegerField(
        default=1,
    )

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.EASY,
    )

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    @property
    def total_time(self):
        """
        Return the total preparation and cooking time in minutes.
        """
        return self.preparation_time + self.cooking_time

    def save(self, *args, **kwargs):
        """
        Create a unique URL-friendly slug when the recipe is first saved.
        """
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Recipe.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)
