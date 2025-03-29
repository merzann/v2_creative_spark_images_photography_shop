from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product, ShippingRate


def add_to_bag(request, product_id):
    """
    Add a :model:`products.Product` to the shopping bag.

    Handles digital and printed formats, storing related info like
    :model:`products.LicenseType` and print type if applicable.

    **Context:**

    Updates the session-based shopping bag and redirects to view.

    **Redirects:**
    :redirect:`view_bag`
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

    item_key = f"{product_id}-{product_format}"
    if product_format == 'digital' and license_id:
        item_key += f"-{license_id}"
    elif product_format == 'printed' and print_type:
        item_key += f"-{print_type}"

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
    """
    Display the shopping bag with :model:`products.Product` details.

    Calculates pricing, VAT, and totals for each item in the session bag.
    May include configuration from :model:`products.LicenseType`,
    :model:`products.PrintType`, and :model:`products.ProductType`.

    **Context:**

    ``bag_items``
        List of products and their cart configurations.
    ``bag_total``
        Total cost before VAT.
    ``vat``
        Calculated VAT based on a 21% rate.
    ``grand_total``
        Final price including VAT.

    **Template:**
    :template:`bag/bag.html`
    """
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    VAT_RATE = 0.21

    for key, item in bag.items():
        product = get_object_or_404(Product, pk=item['product_id'])
        price = float(product.price)
        quantity = item['quantity']
        subtotal = price * quantity

        # Add shipping cost only for printed items
        shipping_cost = 0
        if item.get('format') == 'printed':
            print_type_name = item.get('print_type')
            shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(print_type_name)
            if shipping_key:
                shipping_obj = ShippingRate.objects.filter(product_type=shipping_key).first()
                if shipping_obj:
                    shipping_cost = float(shipping_obj.price) * quantity
                    total_shipping += shipping_cost

        total += subtotal

        bag_items.append({
            'key': key,
            'product': product,
            'quantity': quantity,
            'format': item.get('format'),
            'license': item.get('license'),
            'print_type': item.get('print_type'),
            'price': price,
            'subtotal': subtotal,
            'shipping_cost': shipping_cost,
        })

    vat = round(total * VAT_RATE, 2)
    grand_total = total + vat + total_shipping

    # Store the totals in the session
    request.session['bag_total'] = total
    request.session['vat'] = vat
    request.session['shipping_total'] = total_shipping
    request.session['grand_total'] = grand_total

    context = {
        'bag_items': bag_items,
        'bag_total': total,
        'vat': vat,
        'shipping_total': total_shipping,
        'grand_total': grand_total,
    }
    return render(request, 'bag/bag.html', context)


def remove_from_bag(request, item_key):
    """
    Remove a :model:`products.Product` item from the shopping bag.

    Uses a composite key to remove specific configurations of a product.

    **Context:**

    Updates session bag data and redirects back to the bag view.

    **Redirects:**
    :redirect:`view_bag`
    """
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
