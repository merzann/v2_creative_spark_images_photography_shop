from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    """
    Represents a tag for categorizing products.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Unified model for both digital and printed products.
    Supports both digital downloads and physical prints.
    """

    PRODUCT_TYPE_CHOICES = [
        ("digital", "Digital Download"),
        ("printed", "Printed Product"),
    ]

    PRINT_TYPE_CHOICES = [
        ("canvas", "Canvas Wrap"),
        ("framed", "Framed Print"),
        ("mug", "Mug"),
        ("poster", "Poster Print"),
    ]

    LICENSE_CHOICES = [
        ("personal", "Personal License"),
        ("commercial", "Commercial License"),
        ("advertising", "Advertising License"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.CharField(max_length=100)  # Admin Only
    tags = models.ManyToManyField("Tag", blank=True)  # Admin Only
    product_type = models.CharField(
        max_length=10, choices=PRODUCT_TYPE_CHOICES
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Licensing (for digital downloads)
    license_type = models.CharField(
        max_length=20, choices=LICENSE_CHOICES, blank=True, null=True
    )

    # Ratings
    rating = models.DecimalField(
        max_digits=3, decimal_places=2, default=0.0, blank=True, null=True
    )

    # Visibility
    created_at = models.DateTimeField(auto_now_add=True)  # Admin Only

    # Image previews (shown to users in Owl Carousel)
    image_preview = CloudinaryField(
        "image_preview", folder="product_previews"
    )
    image_framed = CloudinaryField(
        "image_framed", folder="product_previews", blank=True, null=True
    )
    image_canvas = CloudinaryField(
        "image_canvas", folder="product_previews", blank=True, null=True
    )
    image_room_mockup = CloudinaryField(
        "image_room_mockup", folder="product_previews", blank=True, null=True
    )

    # Digital File (only for digital products)
    file = CloudinaryField(
        "file",
        resource_type="raw",
        folder="digital_products",
        blank=True,
        null=True,
    )

    # Print options (only for printed products)
    print_type = models.CharField(
        max_length=20, choices=PRINT_TYPE_CHOICES, blank=True, null=True
    )
    size = models.CharField(
        max_length=50, default="Standard", blank=True, null=True
    )
    stock = models.PositiveIntegerField(default=10, blank=True, null=True)

    def price_with_vat(self, vat_rate=0.21):
        """
        Calculates price including VAT.

        Args:
            vat_rate (float, optional): VAT percentage as a decimal.
                Defaults to 0.21 (21%).

        Returns:
            float: Price including VAT.
        """
        return round(self.price * (1 + vat_rate), 2)

    def __str__(self):
        """
        Returns a string representation of the Product instance.

        Returns:
            str: Product title with its type display name.
        """
        return f"{self.title} ({self.get_product_type_display()})"
