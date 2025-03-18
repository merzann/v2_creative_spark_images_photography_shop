from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import SpecialOffer


@admin.register(SpecialOffer)
class SpecialOfferAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the `SpecialOffer` model.

    **Features:**
    - Displays relevant offer details (`text`, `expiry_date`).
    - Orders offers by `expiry_date` in descending order.
    """
    summernote_fields = ('text',)

    list_display = ('text', 'expiry_date')
    ordering = ('-expiry_date',)
