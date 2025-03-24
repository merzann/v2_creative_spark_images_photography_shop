from django.conf import settings
from products.models import Product


def bag_contents(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0
    VAT_RATE = 0.21

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
