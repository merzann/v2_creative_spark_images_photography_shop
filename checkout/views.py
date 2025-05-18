from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
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
        "checkout/includes/user_form.html",
        {"user": request.user}
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

    Converts session bag to Stripe line items and redirects
    the user to the Stripe-hosted checkout page.
    """
    bag = request.session.get('bag', {})
    line_items = []

    for item in bag.values():
        product = Product.objects.get(id=item['product_id'])
        quantity = item['quantity']
        price = int(float(product.price) * 100)  # convert to cents

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

    Handles both authenticated users and guests, and ensures a
    :model:`user_profiles.UserProfile` exists or is created.
    """
    first_name = request.POST.get("first_name", "").strip()
    last_name = request.POST.get("last_name", "").strip()
    email = request.POST.get("email", "").strip()

    print("\n=== DEBUG: Checkout Profile Save Request ===")
    print("Authenticated:", request.user.is_authenticated)
    print("POST Data:", request.POST)
    print(f"First Name: {first_name}, Last Name: {last_name}, Email: {email}")
    print("===========================================\n")

    # Validate required fields
    if not all([first_name, last_name, email]):
        print("❌ Missing required fields")
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    try:
        if request.user.is_authenticated:
            print("🧾 Handling authenticated user profile save...")
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
            has_profile_data = any(request.POST.get(field) for field in profile_fields)

            if has_profile_data:
                form = UserProfileForm(request.POST, instance=profile)
                if form.is_valid():
                    form.save()
                    print("✅ Authenticated user profile form saved")
                else:
                    print("❌ Invalid form data:", form.errors)
                    return JsonResponse({'error': 'Invalid profile data.'}, status=400)

        else:
            print("🧾 Handling guest user profile save...")

            # Safeguard against empty email
            if '@' not in email:
                raise ValueError("Invalid email address format")

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
            print(f"✅ Guest user created: {user.username}")

            UserProfile.objects.get_or_create(user=user)
            print("✅ Guest UserProfile created or already existed")

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print("✅ Guest user logged in successfully")

        print("✅ Returning success response\n")
        return JsonResponse({'success': True})

    except Exception as e:
        import traceback
        print("❌ Exception occurred during profile save:")
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)
