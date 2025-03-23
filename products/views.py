from django.shortcuts import render, get_object_or_404
from .models import Product, LicenseType, ShippingRate


def product_detail(request, product_id):
    """
    Display details for a single :model:`products.Product`.

    Includes product info and a default shipping cost (currently
    hardcoded to "poster").

    **Context:**

    ``product``
        An instance of :model:`products.Product` identified by its ID.
    ``shipping_cost``
        Flat shipping price for the product (as a float).

    **Template:**

    :template:`products/product_detail.html`
    """
    product = get_object_or_404(Product, id=product_id)
    default_shipping = (
        ShippingRate.objects
        .filter(product_type="poster")  # adjust dynamically in future
        .first()
    )
    shipping_cost = default_shipping.price if default_shipping else 0

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "shipping_cost": float(shipping_cost),  # Pass to template
        },
    )


def image_licenses(request):
    """
    Display a list of active :model:`products.LicenseType` options.

    Typically used as an include/partial view in product-related
    templates.

    **Context:**

    ``licenses``
        A queryset of active :model:`products.LicenseType` instances.

    **Template:**

    :template:`products/includes/image_licenses.html`
    """
    licenses = LicenseType.objects.filter(is_active=True)
    return render(
        request,
        "products/includes/image_licenses.html",
        {"licenses": licenses},
    )
