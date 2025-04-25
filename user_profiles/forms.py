from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to update a :model:`user_profiles.UserProfile` instance.

    Includes custom fields for user's first and last name from the
    built-in :model:`auth.User`, as well as editable profile fields
    like phone number, language, and address.

    **Fields:**
    - ``first_name`` and ``last_name`` are added manually from `User`.
    - Remaining fields are taken from the `UserProfile` model.

    **Meta Class:**
    - ``model``: Specifies that this form is associated with the `UserProfile`
      model.
    - ``fields``: Defines which fields from the `UserProfile` model should be
      included in the form.

    **Template:**
    :template:`user_profiles/profile.html`
    """
    first_name = forms.CharField(
        required=False,
        label="First Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First Name"
        }),
    )
    last_name = forms.CharField(
        required=False,
        label="Last Name",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last Name"
        }),
    )

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
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Pre-fill first and last name
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

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
