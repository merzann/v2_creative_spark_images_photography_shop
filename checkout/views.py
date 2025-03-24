from django.shortcuts import render, redirect, get_current_site
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from products.models import Product
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """
    Render the main checkout page.

    **Template:**
    :template:`checkout/checkout.html`
    """
    return render(request, 'checkout/checkout.html')


def checkout_success(request):
    """
    Render the success page after successful payment.

    Also clears the shopping bag from the session.

    **Template:**
    :template:`checkout/checkout_success.html`
    """
    request.session['bag'] = {}
    return render(request, 'checkout/checkout_success.html')


@csrf_exempt
def create_checkout_session(request):
    """
    Create a Stripe checkout session using items in the shopping bag.

    Converts the session bag into Stripe line items and redirects the user
    to Stripe's hosted checkout page.

    **Context:**
    - ``bag``: The session-based shopping cart.
    - ``line_items``: A list of items formatted for Stripe checkout.

    **Redirects:**
    - To Stripe checkout session URL (303 status).
    """
    bag = request.session.get('bag', {})
    line_items = []

    for item in bag.values():
        product = Product.objects.get(id=item['product_id'])
        quantity = item['quantity']
        price = int(float(product.price) * 100)

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


# Webhook view to handle Stripe events
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    # Set your webhook secret
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

    try:
        # Verify the webhook signature
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

    except ValueError as e:
        # Invalid payload
        print('Invalid payload', e)
        return JsonResponse({'status': 'fail'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Invalid signature', e)
        return JsonResponse({'status': 'fail'}, status=400)

    # Handle the event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session.get('customer_email')

        send_confirmation_email(customer_email, session)

    return JsonResponse({'status': 'success'}, status=200)


def send_confirmation_email(customer_email, session):
    """
    Send an email confirmation to the customer after successful payment.
    """
    subject = 'Your Order Confirmation'
    message = f'Thank you for your purchase! Your order ID is {session["id"]}.'

    # Send confirmation email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [customer_email],
    )
