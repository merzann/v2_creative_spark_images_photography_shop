from products.models import Product


def bag_contents(request):
    return {
        'bag_item_count': 0,
        'bag_total': 0,
        'grand_total': 0,
    }


def bag_summary(request):
    bag = request.session.get('bag', {})
    total_items = 0

    for item in bag.values():
        total_items += item.get('quantity', 0)

    # Pull last added product info if it exists
    last_added = request.session.pop('last_added', None)

    return {
        'cart_count': total_items,
        'last_added': last_added,
    }
