from django.contrib import admin
from .models import DigitalProduct, PrintedProduct, OrderModel

admin.site.register(DigitalProduct)
admin.site.register(PrintedProduct)
admin.site.register(OrderModel)
