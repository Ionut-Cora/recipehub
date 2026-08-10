from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


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


class Ingredient(models.Model):
    """
    Represents an ingredient that can be used in multiple recipes.
    """

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = ["name"]

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

    image = models.ImageField(
        upload_to="recipe_images/",
        blank=True,
        null=True,
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


class RecipeIngredient(models.Model):
    """
    Connects a recipe to an ingredient with a quantity and unit.
    """

    class Unit(models.TextChoices):
        GRAM = "g", "g"
        KILOGRAM = "kg", "kg"
        MILLILITRE = "ml", "ml"
        LITRE = "l", "l"
        TEASPOON = "tsp", "tsp"
        TABLESPOON = "tbsp", "tbsp"
        CUP = "cup", "cup"
        PIECE = "piece", "piece"
        SLICE = "slice", "slice"
        CLOVE = "clove", "clove"
        CAN = "can", "can"
        TO_TASTE = "to_taste", "To taste"

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="recipe_ingredients",
    )

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        related_name="recipe_ingredients",
    )

    quantity = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=(
            "Leave empty when using a unit such as 'To taste'."
        ),
    )

    unit = models.CharField(
        max_length=20,
        choices=Unit.choices,
    )

    preparation_note = models.CharField(
        max_length=150,
        blank=True,
        help_text="Optional, for example: chopped or finely sliced.",
    )

    class Meta:
        ordering = ["id"]
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "ingredient"],
                name="unique_ingredient_per_recipe",
            ),
        ]

    def clean(self):
        """
        Validate ingredient quantities and units.
        """

        if self.unit != self.Unit.TO_TASTE and self.quantity is None:
            raise ValidationError(
                {
                    "quantity": (
                        "A quantity is required unless the unit is "
                        "'To taste'."
                    )
                }
            )

        if self.quantity is not None and self.quantity <= 0:
            raise ValidationError(
                {
                    "quantity": "The quantity must be greater than zero."
                }
            )

    def __str__(self):
        return f"{self.ingredient.name} for {self.recipe.title}"


class Comment(models.Model):
    """
    Represents a comment left by a registered user on a recipe.
    """

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipe_comments",
    )

    body = models.TextField(
        max_length=1000,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return (
            f"Comment by {self.author.username} "
            f"on {self.recipe.title}"
        )


class Rating(models.Model):
    """
    Represents a rating given by a registered user to a recipe.
    """

    class Score(models.IntegerChoices):
        ONE = 1, "1 - Poor"
        TWO = 2, "2 - Fair"
        THREE = 3, "3 - Good"
        FOUR = 4, "4 - Very Good"
        FIVE = 5, "5 - Excellent"

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ratings",
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="recipe_ratings",
    )

    score = models.PositiveSmallIntegerField(
        choices=Score.choices,
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    updated_on = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["recipe", "user"],
                name="unique_user_recipe_rating",
            ),
        ]

    def __str__(self):
        return (
            f"{self.user.username} rated "
            f"{self.recipe.title}: {self.score}"
        )
