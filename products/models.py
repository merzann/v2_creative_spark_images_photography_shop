from django.db import models
from cloudinary.models import CloudinaryField


class Tag(models.Model):
    """Represents a product tag."""

    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """Represents a type/category of product."""

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class LicenseType(models.Model):
    """Represents a license type for digital products."""

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Represents a product for sale."""

    PRINT_TYPE_CHOICES = [
        ("canvas", "Canvas Wrap"),
        ("framed", "Framed Print"),
        ("mug", "Mug"),
        ("poster", "Poster Print"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.ForeignKey(
        "shop.ImageTheme", on_delete=models.SET_NULL,
        null=True, blank=True
    )
    tags = models.ManyToManyField("Tag", blank=True)
    product_types = models.ManyToManyField(ProductType, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    license_types = models.ManyToManyField(LicenseType, blank=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=2,
        default=0.0, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    image_preview = CloudinaryField(
        "image_preview", folder="product_previews"
    )
    image_framed = CloudinaryField(
        "image_framed", folder="product_previews",
        blank=True, null=True
    )
    image_canvas = CloudinaryField(
        "image_canvas", folder="product_previews",
        blank=True, null=True
    )
    image_room_mockup = CloudinaryField(
        "image_room_mockup", folder="product_previews",
        blank=True, null=True
    )

    file = CloudinaryField(
        "file", resource_type="raw",
        folder="digital_products",
        blank=True, null=True
    )

    print_type = models.CharField(
        max_length=20, choices=PRINT_TYPE_CHOICES,
        blank=True, null=True
    )
    size = models.CharField(
        max_length=50, default="Standard",
        blank=True, null=True
    )
    stock = models.PositiveIntegerField(
        default=10, blank=True, null=True
    )

    def price_with_vat(self, vat_rate=0.21):
        """Return price including VAT."""
        return round(self.price * (1 + vat_rate), 2)

    def __str__(self):
        """Return string representation of the product."""
        return f"{self.title}"
