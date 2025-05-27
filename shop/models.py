from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from products.models import Product
import random


class ImageTheme(models.Model):
    """
    Represents an image theme category in the gallery.

     **Template:**

    :template:`shop.html`
    """
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image = CloudinaryField("image", folder='themes/', null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


def generate_unique_order_number():
    """
    Generates a unique order number with the prefix 'ORD-' and ensures
    it is unique in the database.
    """
    while True:
        order_number = f"ORD-{random.randint(100000, 999999)}"
        if not OrderModel.objects.filter(order_number=order_number).exists():
            return order_number


class OrderModel(models.Model):
    """
    Stores customer orders containing products, which can be digital
    or printed. Related to :model:`auth.User` and :model:`Product`.
    """

    class Meta:
        verbose_name_plural = "Order History"

    ORDER_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("delivered", "Delivered"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="orders"
    )

    order_number = models.CharField(
        max_length=10,
        unique=True,
        default=generate_unique_order_number,
        editable=False,
    )

    products = models.ManyToManyField(
        "products.Product",
        blank=True,
        related_name="orders",
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


class PolicyPage(models.Model):
    POLICY_CHOICES = [
        ('privacy', 'Privacy Policy'),
        ('cookies', 'Cookie Policy'),
        ('terms', 'Terms & Conditions'),
    ]

    title = models.CharField(
        max_length=50,
        choices=POLICY_CHOICES,
        unique=True
    )
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return dict(self.POLICY_CHOICES).get(self.title, self.title)
