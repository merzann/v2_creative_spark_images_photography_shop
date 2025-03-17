from django.contrib import admin
from .models import SpecialOffer


@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the :model:`SpecialOffer` model.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        ordering (tuple): Specifies the default ordering of offers.
    """
    list_display = ('text', 'expiry_date')
    ordering = ('-expiry_date',)
