from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form to allow users to update their profile.
    Related to :model:`UserProfile`.
    """

    class Meta:
        model = UserProfile
        fields = ["profile_picture", "language_preference"]
