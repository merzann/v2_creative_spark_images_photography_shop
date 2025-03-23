from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import (
    Product, ProductType, PrintType, LicenseType,
    ShippingOption, Tag, TagGroup
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Tag` model.
    Related to :model:`shop.TagGroup`

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    - ``prepopulated_fields``: Automatically creates "slug" from "name" field
    """
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(TagGroup)
class TagGroupAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.TagGroup` model.
    Related to :model:`shop.Tag`

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    """
    list_display = ("name",)


@admin.register(LicenseType)
class LicenseTypeAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the :model:`shop.LicenseType` model.

    **Attributes:**

    - ``list_display``: Shows the license name and description.
    - ``search_fields``: Enables search by license name.
    """

    list_display = ("name", "description")
    search_fields = ("name",)
    summernote_fields = ("description",)


@admin.register(PrintType)
class PrintTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.PrintType` model.

    **Attributes:**

    - ``list_display``: Displays the Print Types available for a product.
    """
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.Product` model.

    **Attributes:**

    - ``list_display``: Displays key product details.
    - ``search_fields``: Enables searching by title and description.
    - ``list_filter``: Enables filtering by related fields.
    - ``filter_horizontal``: Enables horizontal filter for M2M fields.
    """

    list_display = ("title", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("theme", "tags", "product_types", "license_types")
    filter_horizontal = (
        "tags",
        "product_types",
        "license_types",
        "print_types"
    )


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.ProductType` model.

    **Attributes:**

    - ``list_display``: Displays the "name" field in the admin list view.
    """

    list_display = ("name",)


@admin.register(ShippingOption)
class ShippingOptionAdmin(admin.ModelAdmin):
    """
    Admin configuration for the :model:`shop.ShippingOption` model.

    **Attributes:**
    - ``list_display``: Shows country and flat rate in the list view.
    - ``search_fields``: Enables search by country.
    """
    list_display = ("country", "flat_rate")
    search_fields = ("country",)
