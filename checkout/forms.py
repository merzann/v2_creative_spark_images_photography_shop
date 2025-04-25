from django import forms
from user_profiles.models import UserProfile


class BillingForm(forms.ModelForm):
    """
    Form for collecting billing details from
    :model:`user_profiles.UserProfile`.

    Used during checkout to capture address and contact info.

    **Model:**
    :model:`user_profiles.UserProfile`

    **Excludes:**
    - ``user``: Set automatically based on request.
    - ``profile_picture``: Not needed during checkout.
    - ``language_preference``: Not relevant for billing.
    """

    class Meta:
        model = UserProfile
        exclude = ("user", "profile_picture", "language_preference")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'default_phone_number': 'Phone number',
            'default_postcode': 'Postcode',
            'default_town_or_city': 'Town or city',
            'default_street_address1': 'Street address 1',
            'default_street_address2': 'Street address 2',
            'default_county': 'County',
        }

        for field_name, field in self.fields.items():
            if field_name in placeholders:
                field.widget.attrs["placeholder"] = placeholders[field_name]
            field.widget.attrs["class"] = "form-control"
            field.required = True
