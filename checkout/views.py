from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from user_profiles.models import UserProfile
from user_profiles.forms import UserProfileForm
from products.models import Product
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


def load_guest_form(request):
    """
    Load the empty user form for guest checkout.

    **Template:**
    :template:`checkout/includes/user_form.html`
    """
    html = render_to_string(
        'checkout/includes/user_form.html',
        {'user': request.user}
    )
    return HttpResponse(html)


def checkout_success(request):
    """
    Clear the cart session and render the success page.

    **Template:**
    :template:`checkout/checkout_success.html`
    """
    request.session['bag'] = {}
    return render(request, 'checkout/checkout_success.html')


@csrf_exempt
def create_checkout_session(request):
    """
    Create a Stripe Checkout session based on cart items.

    Converts session bag items to Stripe line items and redirects
    the user to Stripe's hosted checkout page.

    **Redirects:**
    - On success: :url:`/checkout/success/`
    - On cancel: :url:`/bag/`
    """
    bag = request.session.get('bag', {})
    line_items = []

    for item in bag.values():
        product = Product.objects.get(id=item['product_id'])
        quantity = item['quantity']
        price = int(float(product.price) * 100)  # Convert to cents

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


@require_POST
@csrf_exempt
def save_profile_from_checkout(request):
    """
    Save user or guest profile from checkout form.

    Handles both authenticated users and guests.
    Ensures a :model:`user_profiles.UserProfile` exists or is created.

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
    Return billing form HTML with pre-filled fields for authenticated users.

    Used during the AJAX-driven checkout flow.

    **Template:**
    :template:`checkout/includes/billing_form.html`
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
    Return billing form HTML with prefilled data for authenticated users.

    Triggered during checkout Step 2 (Billing Info).

    **Template:**
    :template:`checkout/includes/billing_form.html`
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
