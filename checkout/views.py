from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from user_profiles.forms import UserProfileForm
from products.models import Product
import stripe
import string
import random

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


@require_POST
@csrf_exempt
def save_profile_from_checkout(request):
    first_name = request.POST.get("first_name", "").strip()
    last_name = request.POST.get("last_name", "").strip()
    email = request.POST.get("email", "").strip()

    if not all([first_name, last_name, email]):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        if request.user.is_authenticated:
            # Update existing user
            user = request.user
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()

            # Update or create UserProfile
            profile, _ = UserProfile.objects.get_or_create(user=user)

            # Validate profile form only if profile fields are submitted
            profile_fields = [
                'default_phone_number', 'default_country', 'default_postcode',
                'default_town_or_city', 'default_street_address1',
                'default_street_address2', 'default_county'
            ]
            has_profile_data = any(request.POST.get(field) for field in profile_fields)

            if has_profile_data:
                form = UserProfileForm(request.POST, instance=profile)
                if form.is_valid():
                    form.save()
                else:
                    return JsonResponse({'error': 'Invalid profile data.'}, status=400)

        else:
            # Guest flow — create a new user
            username_base = email.split('@')[0]
            username = username_base
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{username_base}{counter}"
                counter += 1

            password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            UserProfile.objects.create(user=user)

            # Optional: auto-login guest
            # from django.contrib.auth import login
            # login(request, user)

        return JsonResponse({'success': True})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
