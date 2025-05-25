from django.contrib import admin
from .models import SpecialOffer


# Register the SpecialOffer model with custom admin configuration
@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    # Columns to display in the admin list view
    list_display = ('text', 'offer_type', 'expiry_date')

    # Default ordering (newest expiry date first)
    ordering = ('-expiry_date',)

    # Filters available in the sidebar
    list_filter = ('offer_type', 'expiry_date')

    # Enable search by text field
    search_fields = ('text',)
