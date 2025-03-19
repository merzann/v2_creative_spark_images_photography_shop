from django.contrib import admin
from .models import SpecialOffer


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `SpecialOffer` model.

    **Features:**
    - Displays relevant offer details (`text`, `expiry_date`).
    - Orders offers by `expiry_date` in descending order.
    """
    list_display = ('text', 'expiry_date')
    ordering = ('-expiry_date',)
