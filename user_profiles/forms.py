from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to allow users to update their profile.

    Related to :model:`UserProfile`.

    **Meta Class:**
    - ``model``: Specifies that this form is associated with the `UserProfile`
      model.
    - ``fields``: Defines which fields from the `UserProfile` model should be
      included in the form.

    **Template:**
    :template:`user_profiles/profile.html`
    """
    class Meta:
        model = UserProfile
        fields = [
            "profile_picture",
            "language_preference",
            "default_phone_number",
            "default_country",
            "default_postcode",
            "default_town_or_city",
            "default_street_address1",
            "default_street_address2",
            "default_county",
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # Set initial email value if available
        if user:
            self.fields["email"] = forms.EmailField(
                initial=user.email, required=True
            )

        # Apply placeholders and styles to all fields dynamically
        for field_name, field in self.fields.items():
            if field_name:
                placeholder_text = field.label
                if field.required:
                    placeholder_text += " *"
                field.widget.attrs["placeholder"] = placeholder_text
                field.widget.attrs["class"] = (
                    "border-black rounded-0 profile-form-input"
                )
