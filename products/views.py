from django.shortcuts import render, get_object_or_404
from .models import Product, LicenseType


def product_detail(request, product_id):
    """
    Display details for a single :model:`products.Product`.

    **Context:**

    ``product``
        An instance of :model:`products.Product` identified by its ID.

    **Template:**

    :template:`products/product_detail.html`
    """
    product = get_object_or_404(Product, id=product_id)
    return render(
        request,
        "products/product_detail.html",
        {"product": product},
    )


def image_licenses(request):
    licenses = LicenseType.objects.filter(is_active=True)
    return render(
        request,
        "products/includes/image_licenses.html",
        {"licenses": licenses},
    )
