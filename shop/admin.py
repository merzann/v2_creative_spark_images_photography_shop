from django.contrib import admin
from .models import OrderModel, ImageTheme


@admin.register(ImageTheme)
class ImageThemeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.ImageTheme` model.

    **Attributes:**

    - ``list_display``: Displays the "title" field in the admin list view.
    - ``prepopulated_fields``: Automatically generates the "slug" field
      based on the "title" field.
    """

    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing orders.
    """
    class Meta:

        css = {
            "all": ("css/admin_custom.css",)
        }

    list_display = ("order_number", "user", "status", "total_price")
    search_fields = ("order_number", "user__username")
    list_filter = ("status", "created_at")
