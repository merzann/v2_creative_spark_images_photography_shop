import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.http import HttpResponse
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    return render(request, 'checkout/checkout.html')


def load_guest_form(request):
    """
    Load the empty user form for guest checkout.

    **Template:**
    :template:`checkout/includes/user_form.html`
    """
    html = render_to_string(
        "checkout/includes/user_form.html",
        {"user": request.user}
    )
    return HttpResponse(html)


def checkout_success(request):
    # clear session cart
    request.session['bag'] = {}
    return render(request, 'checkout/checkout_success.html')


@csrf_exempt
def create_checkout_session(request):
    bag = request.session.get('bag', {})
    line_items = []

    for item in bag.values():
        product = Product.objects.get(id=item['product_id'])
        quantity = item['quantity']
        price = int(float(product.price) * 100)  # cents

        line_items.append({
            'price_data': {
                'currency': 'eur',
                'unit_amount': price,
                'product_data': {
                    'name': product.title,
                },
            },
            'quantity': quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url=request.build_absolute_uri('/checkout/success/'),
        cancel_url=request.build_absolute_uri('/bag/'),
    )
    return redirect(session.url, code=303)
