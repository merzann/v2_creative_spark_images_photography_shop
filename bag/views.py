from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product, ShippingRate, CountryVAT


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


PRINT_TYPE_TO_SHIPPING_TYPE = {
    "Poster Print": "poster",
    "Canvas Wrap": "canvas",
    "Framed Print": "framed",
    "Mug": "mug",
}

DEFAULT_COUNTRY = "Ireland"
DEFAULT_OPTION = "Standard"
FALLBACK_VAT = 0.21


def view_bag(request):
    """
    Display the shopping bag with :model:`products.Product` details.

    Calculates subtotal, country-specific VAT, and shipping totals for
    all items. Supports :model:`products.LicenseType`,
    :model:`products.PrintType`, and :model:`products.ProductType`.

    Shipping is applied only to printed products using
    :model:`shipping.ShippingRate` based on country and print type.

    **Context:**

    ``bag_items``
        List of products with quantity, format, license, and shipping.
    ``bag_total``
        Total cost of items before VAT and shipping.
    ``vat``
        Calculated VAT based on user country or fallback rate.
    ``vat_rate_display``
        VAT rate as an integer percentage for display.
    ``shipping_total``
        Total shipping cost for all printed items.
    ``grand_total``
        Final cost including item total, VAT, and shipping.

    **Template:**
    :template:`bag/bag.html`
    """
    bag = request.session.get('bag', {})
    bag_items = []
    country = request.session.get('country', DEFAULT_COUNTRY)
    vat_rate = FALLBACK_VAT
    total = 0
    total_shipping = 0

    try:
        vat_obj = CountryVAT.objects.get(country__iexact=country)
        vat_rate = float(vat_obj.vat_rate)
    except CountryVAT.DoesNotExist:
        pass

    for key, item in bag.items():
        product = get_object_or_404(Product, pk=item['product_id'])
        price = float(product.price)
        quantity = item['quantity']
        subtotal = price * quantity
        shipping_cost = 0

        if item.get('format') == 'printed':
            print_type_name = item.get('print_type')
            print_type = product.print_types.filter(
                name=print_type_name
            ).first()

            if print_type:
                shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(print_type_name)
                if shipping_key:
                    shipping_obj = ShippingRate.objects.filter(
                        product_type=shipping_key,
                        country=country,
                        shipping_option=DEFAULT_OPTION.lower()
                    ).first()

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
            'print_type_options': [
                pt.name for pt in product.print_types.all()
            ],
            'price': price,
            'subtotal': subtotal,
            'shipping_cost': shipping_cost,
        })

    vat = round(total * vat_rate, 2)
    grand_total = round(total + vat + total_shipping, 2)

    # Store totals in session
    request.session['bag_total'] = total
    request.session['vat'] = vat
    request.session['shipping_total'] = total_shipping
    request.session['grand_total'] = grand_total

    context = {
        'bag_items': bag_items,
        'bag_total': total,
        'vat': vat,
        'vat_rate_display': int(vat_rate * 100),
        'shipping_total': total_shipping,
        'grand_total': grand_total,
    }

    return render(request, 'bag/bag.html', context)


def update_bag_item(request, item_key):
    """
    Update a bag item stored in the session.

    Supports quantity changes and format-specific updates like print type
    for printed products.

    **Context:**

    Updates the session-stored bag and validates quantity and format
    from the POST request.

    **Redirects:**
    :redirect:`view_bag`
    """
    bag = request.session.get('bag', {})

    if item_key not in bag:
        messages.error(request, "Item not found in your bag.")
        return redirect('view_bag')

    new_quantity = request.POST.get('quantity')
    new_format = request.POST.get('format')
    new_print_type = request.POST.get('print_type')  # Optional

    try:
        new_quantity = int(new_quantity)
        if new_quantity < 1 or new_quantity > 10:
            raise ValueError
    except (TypeError, ValueError):
        messages.error(request, "Invalid quantity selected.")
        return redirect('view_bag')

    bag[item_key]['quantity'] = new_quantity
    bag[item_key]['format'] = new_format

    if new_format == 'printed' and new_print_type:
        bag[item_key]['print_type'] = new_print_type
    elif new_format == 'digital':
        bag[item_key]['print_type'] = None

    request.session['bag'] = bag
    messages.success(request, "Item updated.")
    return redirect('view_bag')


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
