from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class SpecialOffer(models.Model):
    """
    Represents a promotional offer in the store,
    supporting multiple offer types.
    """

    OFFER_TYPES = [
        ('free_shipping', 'Free Shipping Over Amount'),
        ('percentage_discount', 'Percentage Discount on Theme'),
        ('buy_x_get_y', 'Buy X Get Y Free'),
    ]

    offer_type = models.CharField(
        max_length=30,
        choices=OFFER_TYPES,
        help_text=(
            "Type of offer being applied."
        )
    )

    text = models.TextField(
        max_length=100,
        help_text="Short description of the offer."
    )

    expiry_date = models.DateTimeField(
        help_text="Datetime when the offer becomes inactive."
    )

    # Free shipping threshold (e.g., €50 for free shipping)
    min_amount = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
        help_text=(
            "Minimum amount required for offer to apply "
            "(used for free shipping)."
        )
    )

    # Discount percentage for themed promotions
    discount_percentage = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=(
            "Percentage discount to apply "
            "(used with theme-based offers)."
        )
    )

    # Target theme for the discount
    theme = models.ForeignKey(
        "shop.ImageTheme",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=(
            "Theme the discount applies to "
            "(used with percentage discounts)."
        )
    )

    # Quantity conditions for Buy X Get Y Free promotions
    buy_quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=(
            "Quantity to buy to trigger offer "
            "(used for Buy X Get Y)."
        )
    )

    get_quantity = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=(
            "Quantity to get free "
            "(used for Buy X Get Y)."
        )
    )

    def is_active(self):
        """
        Returns True if the offer is still valid (not expired).
        """
        return self.expiry_date >= timezone.now()

    def __str__(self):
        """
        String representation showing the offer text and human-readable type.
        """
        return f"{self.text} (Type: {self.get_offer_type_display()})"


class AboutUs(models.Model):
    title = models.CharField(
        max_length=100,
        default="About Creative Spark Images"
    )
    content = models.TextField(help_text="This is the About Us section text.")
    image = CloudinaryField('image', blank=True, null=True)

    class Meta:
        verbose_name = "About Us Content"
        verbose_name_plural = "About Us Content"

    def __str__(self):
        return self.title
