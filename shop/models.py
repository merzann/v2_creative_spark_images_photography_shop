from django.db import models
from django.contrib.auth.models import User
import random
from cloudinary.models import CloudinaryField


class DigitalProduct(models.Model):
    """
    Stores digital photography products available for purchase and download.
    Related to :model:`auth.User` via orders.
    """

    LICENSE_CHOICES = [
        ("personal", "Personal License"),
        ("commercial", "Commercial License"),
        ("advertising", "Advertising License"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    license_type = models.CharField(
        max_length=20, choices=LICENSE_CHOICES, default="personal"
    )
    image_preview = CloudinaryField("image_preview", folder="digital_previews")
    file = CloudinaryField(
        "file",
        resource_type="raw",
        folder="digital_products",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the title and license type of the digital product."""
        return f"{self.title} ({self.get_license_type_display()})"


class PrintedProduct(models.Model):
    """
    Stores printed versions of photography products available for order.
    Related to :model:`auth.User` via orders.
    """
    PRINT_TYPE_CHOICES = [
        ("canvas", "Canvas Wrap"),
        ("framed", "Framed Print"),
        ("mug", "Mug"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    theme = models.CharField(max_length=100)
    print_type = models.CharField(max_length=20, choices=PRINT_TYPE_CHOICES)
    size = models.CharField(max_length=50, default="Standard")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=10)

    # Cloudinary image preview for the product
    image_preview = CloudinaryField("image_preview", folder="printed_previews")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns the title, print type, and size of the printed product."""
        return f"{self.title} ({self.get_print_type_display()}) - {self.size}"


def generate_unique_order_number():
    """
    Generates a unique order number with the prefix 'ORD-'
    and ensures it is unique in the database.
    """
    while True:
        order_number = f"ORD-{random.randint(100000, 999999)}"
        if not OrderModel.objects.filter(order_number=order_number).exists():
            return order_number


class OrderModel(models.Model):
    """
    Stores customer orders containing digital and/or printed products.
    Related to :model:`auth.User`, :model:`DigitalProduct`,
    and :model:`PrintedProduct`.
    """

    ORDER_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    order_number = models.CharField(
        max_length=10,
        unique=True,
        default=generate_unique_order_number,
        editable=False,
    )

    digital_products = models.ManyToManyField(
        "DigitalProduct",
        blank=True,
    )

    printed_products = models.ManyToManyField(
        "PrintedProduct",
        blank=True,
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default="pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the order number, status, and user who placed the order.
        """
        return (
            f"Order {self.order_number} - {self.get_status_display()} "
            f"({self.user.username})"
        )
