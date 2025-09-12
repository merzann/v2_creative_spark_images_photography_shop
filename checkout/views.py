from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.template.loader import render_to_string
from django.template.exceptions import (
    TemplateDoesNotExist, TemplateSyntaxError
)
from smtplib import SMTPException
from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.http import HttpResponse, JsonResponse

from user_profiles.models import UserProfile
from user_profiles.forms import UserProfileForm
from home.models import SpecialOffer
from products.models import CountryVAT, Product, ShippingRate
from shop.models import OrderModel

from decimal import Decimal
import json
import stripe
import string
import random

stripe.api_key = settings.STRIPE_SECRET_KEY


def checkout(request):
    """
    Render the main checkout page.

    **Template:**
    :template:`checkout/checkout.html`
    """
    return render(request, 'checkout/checkout.html')


def load_checkout_choice(request):
    """
    Render user checkout choice

    **Template:**
    :template:`checkout/checkout_choice.html`
    """
    return render(request, 'checkout/checkout_choice.html')


def checkout_guest_view(request):
    """
    Render guest checkout choice

    **Template:**
    :template:`checkout/checkout.html`
    """
    request.session['guest_checkout'] = True
    return redirect('checkout')


def load_guest_form(request):
    """
    Render and return an empty user form for guest checkout.

    Template:
        checkout/includes/user_form.html

    Returns:
        HttpResponse: Rendered HTML form for the guest user.
    """
    html = render_to_string(
        'checkout/includes/user_form.html',
        {'user': request.user},
        request=request
    )
    return HttpResponse(html)


@csrf_exempt
def create_checkout_session(request):
    """
    Create a Stripe Checkout session based on cart items.

    Converts session bag items to Stripe line items and redirects
    the user to Stripe's hosted checkout page.

    Models:
        products.Product

    **Redirects:**
    - On success: :url:`/checkout/success/`
    - On cancel: :url:`/bag/`
    """
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
                    'images': [request.build_absolute_uri(
                        product.image_preview.url
                    )],
                },
            },
            'quantity': quantity,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        customer_email=(
            request.user.email
            if request.user.is_authenticated
            else request.POST.get("email", "")
        ),
        success_url=(
            request.build_absolute_uri('/checkout/success/')
            + '?session_id={CHECKOUT_SESSION_ID}'
        ),
        cancel_url=request.build_absolute_uri('/checkout/summary/'),
        metadata={
            "bag": json.dumps(request.session.get("bag", {})),
            "user_email": (
                request.user.email
                if request.user.is_authenticated
                else request.POST.get("email", "")
            ),
        }
    )

    # Return session ID as JSON for JS redirect
    return JsonResponse({'id': session.id})


def apply_special_offer(bag_items, bag_total, shipping_total):
    """
    Applies an active special offer to the bag.

    - function checks for a valid SpecialOffer
    based on the current datetime, and applies one of the following:
    - Free shipping if a minimum spend threshold is met
    - Percentage discount on items from a specific theme
    - Buy X Get Y Free on eligible product quantities

    Models:
        offers.SpecialOffer

    Args:
        bag_items: List of items in the shopping bag.
        bag_total: Decimal representing the total cost of items.
        shipping_total: Decimal representing the shipping cost.

    Returns:
        Tuple containing:
        - Updated bag total after discount
        - Updated shipping total
        - Calculated discount
        - The applied SpecialOffer object or None
    """
    active_offer = SpecialOffer.objects.filter(
        expiry_date__gte=now()
    ).order_by('-expiry_date').first()

    discount = Decimal("0.00")

    if not active_offer:
        return bag_total, shipping_total, discount, None

    if (active_offer.offer_type == 'free_shipping'
            and bag_total >= active_offer.min_amount):
        # Apply free shipping if minimum spend threshold is met
        shipping_total = Decimal("0.00")

    elif (active_offer.offer_type == 'percentage_discount'
          and active_offer.theme):
        # Apply percentage discount to themed products
        for item in bag_items:
            if item["product"].theme == active_offer.theme:
                item_total = item["product"].price * item["quantity"]
                discount += item_total * (
                    Decimal(active_offer.discount_percentage) / 100
                )

    elif active_offer.offer_type == 'buy_x_get_y':
        # Apply Buy X Get Y logic
        for item in bag_items:
            if item["quantity"] >= (
                active_offer.buy_quantity + active_offer.get_quantity
            ):
                free_units = item["quantity"] // (
                    active_offer.buy_quantity + active_offer.get_quantity
                )
                discount += free_units * item["product"].price

    new_total = bag_total - discount

    return new_total, shipping_total, discount, active_offer


@require_POST
@csrf_exempt
def save_profile_from_checkout(request):
    """
    Save user or guest profile from checkout form.

    Handles both authenticated users and guests.
    Ensures a :model:`user_profiles.UserProfile` exists or is created.

    Models:
        auth.User
        user_profiles.UserProfile

    **Returns:**
    - JSON success or error message
    """
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    email = request.POST.get('email', '').strip()

    if not all([first_name, last_name, email]):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        if request.user.is_authenticated:
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            profile, _ = UserProfile.objects.get_or_create(user=user)

            profile_fields = [
                'default_phone_number', 'default_country', 'default_postcode',
                'default_town_or_city', 'default_street_address1',
                'default_street_address2', 'default_county'
            ]
            has_profile_data = any(
                request.POST.get(field) for field in profile_fields
            )

            if has_profile_data:
                form = UserProfileForm(request.POST, instance=profile)
                if form.is_valid():
                    form.save()
                else:
                    return JsonResponse(
                        {'error': 'Invalid profile data.'}, status=400
                    )
        else:
            if '@' not in email:
                raise ValueError('Invalid email address format')

            username_base = email.split('@')[0]
            username = username_base
            counter = 1

            while User.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1

            password = ''.join(
                random.choices(string.ascii_letters + string.digits, k=12)
            )

            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )

            UserProfile.objects.get_or_create(user=user)

            login(
                request,
                user,
                backend='django.contrib.auth.backends.ModelBackend'
            )

        return JsonResponse({'success': True})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)


@require_GET
def billing_info(request):
    """
    Render billing form HTML with prefilled data for authenticated users.

    Used in AJAX during checkout.

    Models:
        user_profiles.UserProfile

    Template:
        checkout/includes/billing_form.html

    Returns:
        HttpResponse: Rendered billing form.
    """
    initial_data = {}

    if request.user.is_authenticated:
        profile = getattr(request.user, 'userprofile', None)
        if profile:
            initial_data = {
                'billing_street1': profile.default_street_address1,
                'billing_street2': profile.default_street_address2,
                'billing_city': profile.default_town_or_city,
                'billing_county': profile.default_county,
                'billing_postcode': profile.default_postcode,
                'billing_country': profile.default_country,
                'billing_phone': profile.default_phone_number,
            }

    html = render_to_string(
        'checkout/includes/billing_form.html',
        initial_data,
        request=request
    )
    return HttpResponse(html)


@require_GET
def load_billing_form(request):
    """
    Render billing form HTML with pre-filled fields for logged-in users.

    Triggered during step 2 of the checkout process.

    Requires authentication. Maps billing fields to
    :model:`user_profiles.UserProfile`.

    Template:
        checkout/includes/billing_form.html

    Returns:
        HttpResponse: Rendered billing form with initial data.
    """
    initial_data = {}

    if request.user.is_authenticated:
        profile = getattr(request.user, 'userprofile', None)
        if profile:
            initial_data = {
                'billing_street1': profile.default_street_address1,
                'billing_street2': profile.default_street_address2,
                'billing_city': profile.default_town_or_city,
                'billing_county': profile.default_county,
                'billing_postcode': profile.default_postcode,
                'billing_country': profile.default_country,
                'billing_phone': profile.default_phone_number,
            }

    html = render_to_string(
        'checkout/includes/billing_form.html',
        {'initial': initial_data},
        request=request
    )
    return HttpResponse(html)


@require_POST
@csrf_exempt
def save_billing_from_checkout(request):
    """
    Save billing information to the user's profile during checkout.

    Requires authentication. Maps billing fields to
    :model:`user_profiles.UserProfile`.

    **Returns:**
    - JSON success message or error message
    """
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required.'}, status=403)

    try:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        profile.default_street_address1 = request.POST.get(
            'billing_street1', ''
        ).strip()
        profile.default_street_address2 = request.POST.get(
            'billing_street2', ''
        ).strip()
        profile.default_town_or_city = request.POST.get(
            'billing_city', ''
        ).strip()
        profile.default_county = request.POST.get(
            'billing_county', ''
        ).strip()
        profile.default_postcode = request.POST.get(
            'billing_postcode', ''
        ).strip()
        profile.default_country = request.POST.get(
            'billing_country', ''
        ).strip()
        profile.default_phone_number = request.POST.get(
            'billing_phone', ''
        ).strip()

        profile.save()

        return JsonResponse({'success': True})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)


@require_GET
def checkout_summary(request):
    """
    Display the checkout summary view.

    Shows contact info, billing info, shopping cart summary, discounts,
    and a pricing breakdown (net, tax, shipping, total).

    Maps:
    :model:`products.Product`
    :model:`offers.SpecialOffer`
    :model:`user_profiles.UserProfile`
    :model:`shipping.ShippingRate`
    :model:`tax.CountryVAT`

    **Context:**
    - bag_items: List of product line items with prices and quantities
    - bag_total: Total cost before tax and shipping
    - vat: Tax amount
    - vat_rate_display: Tax rate as a percentage (int)
    - shipping_total: Shipping total for all items
    - grand_total: Total including tax and shipping
    - contact_info: Dict of user name/email from session or user
    - billing_info: Dict of billing form fields from session or profile
    - special_offer: Active offer if any

    **Template:**
    :template:`checkout/includes/checkout_summary.html`
    """
    bag = request.session.get("bag", {})
    bag_items = []
    bag_total = Decimal("0.00")
    country = request.session.get('country', DEFAULT_COUNTRY)
    shipping_total = Decimal("0.00")

    try:
        vat_obj = CountryVAT.objects.get(country__iexact=country)
        vat_rate = float(vat_obj.vat_rate)
    except CountryVAT.DoesNotExist:
        pass

    for key, item in bag.items():
        product = get_object_or_404(Product, pk=item["product_id"])
        quantity = item["quantity"]
        unit_price = product.price
        line_total = unit_price * quantity
        bag_total += line_total

        shipping_cost = Decimal("0.00")
        if item.get("format") == "printed":
            print_type_name = item.get("print_type")
            shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(print_type_name)
            if shipping_key:
                shipping_obj = ShippingRate.objects.filter(
                    product_type=shipping_key,
                    country=country,
                    shipping_option=DEFAULT_OPTION.lower()
                ).first()
                if shipping_obj:
                    shipping_cost = shipping_obj.price * quantity
                    shipping_total += shipping_cost

        bag_items.append({
            "key": key,
            "product": product,
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": line_total,
            "format": item.get("format"),
            "license": item.get("license"),
            "print_type": item.get("print_type"),
            "shipping_cost": shipping_cost,
        })

    new_total, shipping_total, discount, special_offer = apply_special_offer(
        bag_items, bag_total, shipping_total
    )

    vat_rate_display = 21
    vat_rate = Decimal(vat_rate_display) / 100
    vat = (new_total * vat_rate).quantize(Decimal("0.01"))
    grand_total = new_total + shipping_total + vat

    contact_info = {
        "first_name": (
            request.user.first_name if request.user.is_authenticated else ""
        ),
        "last_name": (
            request.user.last_name if request.user.is_authenticated else ""
        ),
        "email": (
            request.user.email if request.user.is_authenticated else ""
        ),
    }

    profile = (
        getattr(request.user, "userprofile", None)
        if request.user.is_authenticated else None
    )

    billing_info = {
        "billing_street1": profile.default_street_address1 if profile else "",
        "billing_street2": profile.default_street_address2 if profile else "",
        "billing_city": profile.default_town_or_city if profile else "",
        "billing_county": profile.default_county if profile else "",
        "billing_postcode": profile.default_postcode if profile else "",
        "billing_country": profile.default_country if profile else "",
        "billing_phone": profile.default_phone_number if profile else "",
    }

    context = {
        "bag_items": bag_items,
        "bag_total": bag_total,
        "vat": vat,
        "vat_rate_display": vat_rate_display,
        "shipping_total": shipping_total,
        "grand_total": grand_total,
        "contact_info": contact_info,
        "billing_info": billing_info,
        "discount": discount,
        "special_offer": special_offer,
    }

    return render(
        request,
        "checkout/includes/checkout_summary.html",
        context
    )


PRINT_TYPE_TO_SHIPPING_TYPE = {
    "Poster Print": "poster",
    "Canvas Wrap": "canvas",
    "Framed Print": "framed",
    "Mug": "mug",
}

DEFAULT_COUNTRY = "Ireland"
DEFAULT_OPTION = "Standard"
FALLBACK_VAT = 0.21


@csrf_exempt
def stripe_webhook(request):
    """
    Process incoming Stripe webhook events.

    Primarily listens for `checkout.session.completed` events to:
    - Create orders
    - Attach products
    - Trigger confirmation email

    Related to models:
    :model:`auth.User`
    :model:`orders.OrderModel`
    :model:`products.Product`

    Returns:
        HttpResponse: 200 if handled, 400 if error in payload/signature.
    """
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")
    wh_secret = settings.STRIPE_WH_SECRET

    try:
        # Verify the webhook signature and construct event
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        metadata = session.get("metadata", {})

        user_id = metadata.get("user_id")
        user_email = metadata.get("user_email")

        # Try to fetch the user by ID first, fallback to email
        user = None
        if user_id:
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                pass

        if not user and user_email:
            user = User.objects.filter(email=user_email).first()

        # If user is still not found, do not create order
        if not user:
            # Return 200 so Stripe doesn't retry
            return HttpResponse(status=200)

        # Get bag (cart) data from metadata
        try:
            bag = json.loads(metadata.get("bag", "{}"))
        except (TypeError, json.JSONDecodeError):
            bag = {}

        # Calculate order total from Stripe session
        order_total = Decimal(session.get("amount_total", 0)) / 100

        # Create order
        order = OrderModel.objects.create(
            user=user,
            total_price=order_total,
            status="completed",
        )

        # Add each product from the bag
        for item in bag.values():
            try:
                product = Product.objects.get(id=item["product_id"])
                order.products.add(product)
            except Product.DoesNotExist:
                continue

        order.save()

        # Fallback email in case template loader fails
        try:
            send_order_email(user, order, session.get("id"))
        except (TemplateDoesNotExist, TemplateSyntaxError, SMTPException) as e:
            print(f"[EMAIL ERROR] Failed to send rich confirmation email: {e}")

            send_mail(
                subject=f"Your Order {order.order_number} – Confirmation",
                message=(
                    f"Thank you for your order. Your order number is "
                    f"{order.order_number}.\n"
                    f"If you have questions, reply to this email.\n\n"
                    f"Your Creative Spark Images Team"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )

    return HttpResponse(status=200)


def checkout_success(request):
    """
    Clears cart and displays order summary with downloads if applicable.

    Uses:
        - Stripe session to fetch metadata and user.
        - Prefilled user billing info and product list.

    Related to models:
    :model:`auth.User`
    :model:`orders.OrderModel`
    :model:`user_profiles.UserProfile`
    :model:`products.Product`
    :model:`tax.CountryVAT`
    :model:`shipping.ShippingRate`
    :model:`offers.SpecialOffer`

    Template:
        checkout/includes/checkout_success.html

    Returns:
        HttpResponse: Rendered success page.
    """
    session_id = request.GET.get('session_id')
    if not session_id:
        return HttpResponse("Missing session ID", status=400)

    try:
        session = stripe.checkout.Session.retrieve(session_id)
        customer_email = session.get("customer_email")
        user = User.objects.filter(email=customer_email).first()
        if not user:
            return HttpResponse("User not found", status=404)
        order = OrderModel.objects.filter(user=user).latest("created_at")
    except Exception as e:
        return HttpResponse(f"Error fetching order: {str(e)}", status=500)

    try:
        bag = json.loads(session.get("metadata", {}).get("bag", "{}"))
    except (TypeError, json.JSONDecodeError):
        bag = {}

    download_links = []
    for product in order.products.all():
        if product.file:
            url = product.file.build_url(
                resource_type='raw',
                type='upload',
                secure=True,
                transformation=[
                    {'flags': f'attachment:{product.title.replace(" ", "_")}'}
                ],
                expires=3600
            )
            download_links.append({"title": product.title, "url": url})

    request.session["bag"] = {}

    bag_items = []
    bag_total = Decimal("0.00")
    country = request.session.get('country', DEFAULT_COUNTRY)
    shipping_total = Decimal("0.00")

    try:
        vat_obj = CountryVAT.objects.get(country__iexact=country)
        vat_rate = float(vat_obj.vat_rate)
    except CountryVAT.DoesNotExist:
        pass

    for key, item in bag.items():
        product = get_object_or_404(Product, pk=item["product_id"])
        quantity = item["quantity"]
        unit_price = product.price
        line_total = unit_price * quantity
        bag_total += line_total

        shipping_cost = Decimal("0.00")
        if item.get("format") == "printed":
            print_type_name = item.get("print_type")
            shipping_key = PRINT_TYPE_TO_SHIPPING_TYPE.get(print_type_name)
            if shipping_key:
                shipping_obj = ShippingRate.objects.filter(
                    product_type=shipping_key,
                    country=country,
                    shipping_option=DEFAULT_OPTION.lower()
                ).first()
                if shipping_obj:
                    shipping_cost = shipping_obj.price * quantity
                    shipping_total += shipping_cost

        bag_items.append({
            "product": product,
            "license": item.get('license'),
            "print_type": item.get("print_type"),
            "quantity": quantity,
            "unit_price": unit_price,
            "line_total": line_total,
            "shipping_cost": shipping_cost,
        })

    new_total, shipping_total, discount, special_offer = apply_special_offer(
        bag_items, bag_total, shipping_total
    )

    vat_rate_display = 21
    vat_rate = Decimal(vat_rate_display) / 100
    vat = (new_total * vat_rate).quantize(Decimal("0.01"))
    grand_total = (new_total + vat + shipping_total).quantize(Decimal("0.01"))

    profile = getattr(user, "userprofile", None)

    billing_info = {
        "billing_street1": profile.default_street_address1 if profile else "",
        "billing_street2": profile.default_street_address2 if profile else "",
        "billing_city": profile.default_town_or_city if profile else "",
        "billing_county": profile.default_county if profile else "",
        "billing_postcode": profile.default_postcode if profile else "",
        "billing_country": profile.default_country if profile else "",
        "billing_phone": profile.default_phone_number if profile else "",
    }

    send_order_email(user, order, {
        "bag_items": bag_items,
        "grand_total": grand_total,
        "shipping_total": shipping_total,
        "vat": vat,
        "discount": discount,
    })

    return render(
        request,
        "checkout/includes/checkout_success.html",
        {
            "order": order,
            "download_links": download_links,
            "bag_items": bag_items,
            "bag_total": bag_total,
            "vat": vat,
            "vat_rate_display": vat_rate_display,
            "shipping_total": shipping_total,
            "grand_total": grand_total,
            "billing_info": billing_info,
            "discount": discount,
            "special_offer": special_offer,
            "step": 5,
        }
    )


def send_order_email(user, order, summary):
    """
    Send order confirmation email with HTML formatting.

    Args:
        user (User): The user who placed the order.
        order (OrderModel): The completed order object.
        summary (dict): Bag items and totals.
    """
    subject = "Order Confirmation"
    to_email = [user.email]
    from_email = settings.DEFAULT_FROM_EMAIL

    download_links = []
    for product in order.products.all():
        if product.file:
            url = product.file.build_url(
                resource_type='raw',
                type='upload',
                transformation=[
                    {'flags': f'attachment:{product.title.replace(" ", "_")}'}
                ],
                expires=3600
            )
            download_links.append({"title": product.title, "url": url})

    context = {
        "user": user,
        "order": order,
        "download_links": download_links,
        **summary,
    }

    text_content = render_to_string(
        "checkout/email/order_confirmation_email.txt",
        context
    )

    html_content = render_to_string(
        "checkout/email/order_confirmation_email.html",
        context
    )

    # Compose and send email with both formats
    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=from_email,
        to=to_email
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
