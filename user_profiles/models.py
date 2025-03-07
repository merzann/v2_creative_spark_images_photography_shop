from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    Extends the default Django User model to include additional user details.
    Related to :model:`auth.User`.
    """

    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("de", "German"),
        ("fr", "French"),
        ("es", "Spanish"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField("profile_pictures", blank=True, null=True)
    language_preference = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default="en")

    def __str__(self):
        """Returns the username of the user profile."""
        return f"Profile of {self.user.username}"

    def get_order_history(self):
        """Returns all past orders made by this user."""
        return self.user.ordermodel_set.all()
