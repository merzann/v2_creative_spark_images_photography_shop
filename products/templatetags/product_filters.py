from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiply the value by the arg"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''


@register.filter
def get_range(value, max_val=None):
    """
    Return a range from 1 to value (or 1 to min(value, max_val))
    Usage: {% for i in product.stock|get_range:10 %}
    """
    try:
        value = int(value)
        max_val = int(max_val) if max_val is not None else value
        return range(1, min(value, max_val) + 1)
    except Exception:
        return []
