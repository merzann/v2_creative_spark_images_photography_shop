from django.conf import settings
from products.models import Product
from decimal import Decimal


def bag_contents(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = Decimal("0.00")
    VAT_RATE = Decimal("0.21")

    for item_id, item in bag.items():
        try:
            product = Product.objects.get(id=item['product_id'])
            quantity = item['quantity']
            subtotal = product.price * quantity
            total += subtotal

            bag_items.append({
                'product': product,
                'quantity': quantity,
                'format': item.get('format'),
                'license': item.get('license'),
                'print_type': item.get('print_type'),
                'subtotal': subtotal,
            })
        except Product.DoesNotExist:
            continue

    vat = total * VAT_RATE
    grand_total = total + vat

    return {
        'bag_items': bag_items,
        'bag_total': total,
        'vat': vat,
        'grand_total': grand_total,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }


def bag_summary(request):
    bag = request.session.get('bag', {})
    total_items = 0

    for item in bag.values():
        total_items += item.get('quantity', 0)

    return {
        'cart_count': total_items,
    }
