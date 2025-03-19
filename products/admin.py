from django.contrib import admin
from products.models import Product, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Tag` model.

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    """

    list_display = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Product` model.

    **Attributes:**

    - ``list_display``: Displays key product details (title, price,
      creation date) in the admin list view.
    - ``search_fields``: Allows searching by title and description.
    - ``list_filter``: Enables filtering products by theme and tags.
    """
    list_display = ("title", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("theme", "tags")
