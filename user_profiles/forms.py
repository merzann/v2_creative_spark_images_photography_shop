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
        super().__init__(*args, **kwargs)

        # Custom placeholder text mapping
        placeholders = {
            'default_phone_number': 'Phone number',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town or city',
            'default_street_address1': 'Street address 1',
            'default_street_address2': 'Street address 2',
            'default_county': 'County',
        }

        # Apply placeholders dynamically
        for field_name, field in self.fields.items():
            if field_name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[field_name]
            field.widget.attrs["class"] = "form-control"
