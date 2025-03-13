from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to allow users to update their profile.
    Related to :model:`UserProfile`.
    """
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email address",
            "class": "form-control",
            "aria-label": "Email Address"
        })
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
        """
        Customizes form fields with placeholders and validation.
        """
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields["email"].initial = user.email

    def clean_email(self):
        """
        Ensure email is unique and not already used by another user.
        """
        email = self.cleaned_data.get("email")
        if User.objects.exclude(pk=self.instance.user.pk).filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email
