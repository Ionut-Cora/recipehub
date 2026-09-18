from allauth.account.forms import LoginForm, SignupForm
from django import forms
from .models import Comment, Rating, Recipe, RecipeIngredient


class RecipeHubSignupForm(SignupForm):
    """
    Add Bootstrap classes to the Allauth registration form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                }
            )


class RecipeHubLoginForm(LoginForm):
    """
    Add Bootstrap classes to the Allauth login form.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.widget.input_type != "checkbox":
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                    }
                )


class RecipeForm(forms.ModelForm):
    """
    Form used by authenticated users to create and edit recipes.
    """

    class Meta:
        model = Recipe
        fields = [
            "category",
            "title",
            "summary",
            "image",
            "instructions",
            "preparation_time",
            "cooking_time",
            "servings",
            "difficulty",
            "status",
        ]

        widgets = {
            "category": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Recipe title",
                }
            ),
            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Write a short recipe summary",
                }
            ),
            "image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Explain how to prepare the recipe",
                }
            ),
            "preparation_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),
            "cooking_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                }
            ),
            "servings": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                }
            ),
            "difficulty": forms.Select(
                attrs={"class": "form-select"}
            ),
            "status": forms.Select(
                attrs={"class": "form-select"}
            ),
        }


class RecipeIngredientForm(forms.ModelForm):
    """
    Form for adding an ingredient to a recipe.
    Users enter the ingredient name manually.
    """

    ingredient_name = forms.CharField(
        max_length=100,
        label="Ingredient",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "e.g. Bacon",
            }
        ),
    )

    class Meta:
        model = RecipeIngredient
        fields = [
            "quantity",
            "unit",
            "preparation_note",
        ]

        widgets = {
            "quantity": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "0.01",
                    "step": "0.01",
                    "placeholder": "Quantity",
                }
            ),
            "unit": forms.Select(
                attrs={"class": "form-select"}
            ),
            "preparation_note": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. chopped",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk and self.instance.ingredient_id:
            self.fields["ingredient_name"].initial = (
                self.instance.ingredient.name
            )


RecipeIngredientFormSet = forms.inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=1,
    can_delete=True,
)
        

class CommentForm(forms.ModelForm):
    """
    Form used by authenticated users to comment on recipes.
    """

    class Meta:
        model = Comment
        fields = [
            "body",
        ]

        widgets = {
            "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Share your thoughts about this recipe...",
                }
            ),
        }

        labels = {
            "body": "Your comment",
        }


class RatingForm(forms.ModelForm):
    """
    Form used by authenticated users to rate a recipe.
    """

    class Meta:
        model = Rating
        fields = [
            "score",
        ]

        widgets = {
            "score": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

        labels = {
            "score": "Your rating",
        }
