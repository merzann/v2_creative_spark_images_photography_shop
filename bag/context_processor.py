def bag_contents(request):
    bag = request.session.get('bag', {})
    item_count = sum(item['quantity'] for item in bag.values())

    return {
        'bag_items': bag,
        'bag_item_count': item_count,
    }
