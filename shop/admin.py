from django.contrib import admin
from .models import DigitalProduct, PrintedProduct, OrderModel

admin.site.register(DigitalProduct)
admin.site.register(PrintedProduct)


class OrderModelAdmin(admin.ModelAdmin):
    """Customizes OrderModel name in Admin Panel"""
    class Media:
        css = {
            "all": ("css/admin_custom.css",)
        }

    model = OrderModel
    verbose_name_plural = "Order History"


admin.site.register(OrderModel, OrderModelAdmin)
