from django.contrib import admin
from .models import OrderModel


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
