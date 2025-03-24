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

    product_format = request.POST.get('format')
    license_id = request.POST.get('license')
    print_type_raw = request.POST.get('print_type')

    license_name = None
    print_type_name = None

    if license_id and product_format == 'digital':
        try:
            license_obj = product.license_types.get(id=license_id)
            license_name = license_obj.name
        except Exception:
            license_name = "Unknown License"

    if print_type_raw and product_format == 'printed':
        print_type_name = print_type_raw.strip()


    # Create a composite item key
    item_key = f"{product_id}-{product_format}"
    if product_format == 'digital' and license_id:
        item_key += f"-{license_id}"
    elif product_format == 'printed' and print_type:
        item_key += f"-{print_type}"

    # Add or update the item in the bag
    if item_key in bag:
        bag[item_key]['quantity'] += quantity
    else:
        bag[item_key] = {
            'product_id': product_id,
            'format': product_format,
            'license': license_name,
            'print_type': print_type_name,
            'quantity': quantity,
        }

    request.session['bag'] = bag
    messages.success(request, "Product added to your cart!")
    return redirect("view_bag")


def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []

    for key, item in bag.items():
        product = get_object_or_404(Product, pk=item['product_id'])

        bag_items.append({
            'key': key,
            'product': product,
            'quantity': item['quantity'],
            'format': item.get('format'),
            'license': item.get('license'),
            'print_type': item.get('print_type'),
        })

    return render(request, 'bag/bag.html', {'bag_items': bag_items})


def remove_from_bag(request, item_key):
    """Remove a specific item from the bag using its composite key."""
    try:
        bag = request.session.get("bag", {})
        if item_key in bag:
            bag.pop(item_key)
            request.session["bag"] = bag
            messages.success(request, "Item removed from your bag.")
        else:
            messages.warning(request, "Item not found in your bag.")
    except Exception:
        messages.error(request, "Error removing item from bag.")
    return redirect("view_bag")
