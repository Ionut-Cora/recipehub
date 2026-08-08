from allauth.account.forms import LoginForm, SignupForm


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
