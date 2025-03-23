from django.shortcuts import render, get_object_or_404
from .models import Product, LicenseType, ShippingRate
import json


PRINT_TYPE_TO_SHIPPING_TYPE = {
    "Poster Print": "poster",
    "Canvas Wrap": "canvas",
    "Framed Print": "framed",
    "Mug": "mug",
}


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
    shipping_rates = {}

    # Build shipping rates dict using matching PrintType
    for print_type in product.print_types.all():
        name = str(print_type.name)
        print(f"PrintType: {print_type.name}")
        shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(name)
        print(f"→ Mapped to shipping_key: {shipping_key}")

        if shipping_key:
            rate = (
                ShippingRate.objects
                .filter(product_type=shipping_key)
                .first()
            )
            print(f"→ Found rate: {rate.price if rate else 'None'}")
            if rate:
                shipping_rates[name] = float(rate.price)

    default_shipping_cost = next(iter(shipping_rates.values()), 0.00)

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product,
            "shipping_cost": default_shipping_cost,
            "shipping_rates": json.dumps(shipping_rates),
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
