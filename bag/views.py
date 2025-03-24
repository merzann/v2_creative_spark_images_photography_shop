from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.urls import reverse


def add_to_bag(request, product_id):
    """
    Add a product to the shopping bag.
    Stores quantity and configuration (license/print type).
    """
    product = get_object_or_404(Product, pk=product_id)
    bag = request.session.get("bag", {})
    raw_quantity = int(request.POST.get('quantity'))
    product_format = request.POST.get('format')
    license_id = request.POST.get('license')
    print_type = request.POST.get('print_type')

    if not raw_quantity:
        messages.error(request, "Quantity is required.")
        return redirect("product_detail", product_id=product_id)

    try:
        quantity = int(raw_quantity)
    except ValueError:
        messages.error(request, "Invalid quantity.")
        return redirect("product_detail", product_id=product_id)

    # Add or update item
    if str(product_id) in bag:
        bag[str(product_id)]["quantity"] += quantity
    else:
        bag[str(product_id)] = {
            "product_id": product_id,
            "quantity": quantity,
            "format": product_format,
        }

    request.session["bag"] = bag
    messages.success(request, "Product added to your cart!")
    return redirect("view_bag")


def view_bag(request):
    """
    Show the contents of the bag.
    """
    bag = request.session.get('bag', {})
    return render(request, 'bag/bag.html', {'bag': bag})


def remove_from_bag(request, product_id):
    """ Remove item from shopping bag """
    try:
        bag = request.session.get("bag", {})
        if str(product_id) in bag:
            bag.pop(str(product_id))
            request.session["bag"] = bag
            messages.success(request, "Item removed from your bag.")
        return redirect("view_bag")
    except Exception:
        messages.error(request, "Error removing item.")
        return redirect("view_bag")
