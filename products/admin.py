from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing products.
    """
    list_display = ("title", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("theme", "tags")
