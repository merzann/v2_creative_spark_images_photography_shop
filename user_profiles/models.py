from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django_countries.fields import CountryField
from products.models import Product


class UserProfile(models.Model):
    """
    Extends the default Django User model to include additional user details.
    Related to :model:`auth.User`.
    """

    class Meta:
        verbose_name_plural = "User Profiles"

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


class Wishlist(models.Model):
    """
    Stores a user's wishlist items.
    Related to :model:`auth.User` and :model:`products.Product`.
    """

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="wishlist"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="wishlisted_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")
        ordering = ["-added_at"]

    def __str__(self):
        return f"{self.user.username}'s wishlist item: {self.product.title}"
