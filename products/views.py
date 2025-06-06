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

    for print_type in product.print_types.all():
        name = str(print_type.name)
        shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(name)
        if shipping_key:
            rate = (
                ShippingRate.objects
                .filter(product_type=shipping_key)
                .first()
            )
            if rate:
                shipping_rates[name] = float(rate.price)

    bag = request.session.get("bag", {})
    digital_in_cart = 0
    printed_in_cart = 0

    for key, item in bag.items():
        if str(item.get('product_id')) == str(product.id):
            if item.get("format") == "digital":
                digital_in_cart += item.get("quantity", 0)
            elif item.get("format") == "printed":
                printed_in_cart += item.get("quantity", 0)

    remaining_digital = max(0, 10 - digital_in_cart)
    remaining_printed = max(0, 10 - printed_in_cart)

    return render(request, "products/product_detail.html", {
        "product": product,
        "shipping_rates": json.dumps(shipping_rates),
        "remaining_digital": remaining_digital,
        "remaining_printed": remaining_printed,
    })


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
        "products/image_licenses.html",
        {"licenses": licenses},
    )
