from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField


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
    profile_picture = CloudinaryField(
        "profile_pictures",
        blank=True,
        null=True,
    )
    language_preference = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICES,
        default="en"
    )

    # Contact & Address Fields
    default_phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    default_country = CountryField(
        blank_label="Select Country",
        null=True,
        blank=True,
    )

    default_postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )

    default_town_or_city = models.CharField(
        max_length=40,
        null=True,
        blank=True,
    )

    default_street_address1 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
    )

    default_street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True,
    )

    default_county = models.CharField(
        max_length=80,
        null=True,
        blank=True,
    )

    def __str__(self):
        """Returns the username of the user profile."""
        return f"Profile of {self.user.username}"

    def get_order_history(self):
        """
        Returns all past orders related to :model:`shop.OrderModel`.

        **Context:**
        - ``queryset``: All instances of :model:`shop.OrderModel`
        related to the user.

        **Returns:**
        - ``QuerySet``: A list of the user’s previous orders.
        """
        return self.user.ordermodel_set.all()
