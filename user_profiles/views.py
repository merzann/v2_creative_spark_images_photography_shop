from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.db.models import Prefetch

from .models import Wishlist
from products.models import Product
from shop.models import OrderModel

from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display and update the user's profile and show their order history.

    Handles updates to both :model:`auth.User` and
    :model:`user_profiles.UserProfile`. Also retrieves the user's
    past orders for display.

    **Context:**

    ``form``
        Instance of :form:`user_profiles.UserProfileForm` bound to user.
    ``first_name`` / ``last_name``
        Populated from the base User model.
    ``orders``
        Queryset of :model:`orders.OrderModel` instances linked to user,
        ordered by most recent first.
    ``active_slide``
        Indicates the currently active tab/section in the profile UI.

    **Template:**
    :template:`user_profiles/profile.html`
    """
    user_profile = request.user.userprofile
    user = request.user  # Grab the base User model

    if request.method == "POST":
        form = UserProfileForm(
            request.POST, request.FILES, instance=user_profile
        )

        if form.is_valid():
            try:
                form.save()

                # Also update first_name and last_name from POST data
                user.first_name = request.POST.get("first_name", "").strip()
                user.last_name = request.POST.get("last_name", "").strip()
                user.save()

                messages.success(
                    request, "Your profile has been updated successfully."
                )
            except Exception as e:
                messages.error(
                    request, f"An error occurred: {str(e)}"
                )
            return redirect("profile")
        else:
            messages.warning(request, "Invalid form submission.")
    else:
        form = UserProfileForm(instance=user_profile)

    orders = OrderModel.objects.filter(user=request.user) \
        .prefetch_related(
            Prefetch('products', queryset=Product.objects.all())
        ) \
        .order_by('-created_at')

    active_slide = request.GET.get("slide", "profile")

    return render(
        request,
        "user_profiles/profile.html",
        {
            "form": form,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "orders": orders,
            "active_slide": active_slide,
        },
    )


@login_required
def request_account_deletion(request):
    """
    Handle a user-submitted request to delete their account.

    A POST request triggers an email to the site administrator containing
    the user's information and their optional message.

    **Context:**
    - This view does not render a template. It redirects to the "profile"
      page after handling the request.

    **Behavior:**
    - On success, a success message is shown and the user is redirected.
    - On non-POST requests, the view immediately redirects.

    **Email Content:**
    - Username and email of the requesting user.
    - Optional message provided in the request.

    **Redirects:**
    - :redirect:`profile`
    """
    if request.method == "POST":
        try:
            message = request.POST.get("message", "No message provided.")
            user = request.user
            email_body = (
                f"User {user.username} ({user.email}) has requested "
                f"account deletion.\n\nMessage:\n{message}"
            )

            send_mail(
                subject="Account Deletion Request",
                message=email_body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
            )

            messages.success(
                request,
                "Your request has been submitted successfully."
            )
        except Exception as e:
            messages.error(
                request,
                f"An error occurred: {str(e)}. Please try again."
            )

    return redirect("profile")


@login_required
def wishlist_view(request):
    """
    Display the user's wishlist.

    Retrieves all products saved by the user to their wishlist
    for rendering in the UI.

    **Context:**

    ``wishlist_items``
        Queryset of :model:`user_profiles.Wishlist` entries for the user,
        with related :model:`products.Product` objects prefetched.

    **Template:**
    :template:`user_profiles/includes/wishlist_card.html`
    """
    wishlist_items = (
        Wishlist.objects
        .select_related("product")
        .filter(user=request.user)
    )
    return render(
        request,
        "user_profiles/includes/wishlist_card.html",
        {"wishlist_items": wishlist_items},
    )


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.

    Ensures that the product is linked to the current user's wishlist.
    If the product already exists, it won’t be duplicated.

    **Args:**
    ``product_id``
        Primary key of the :model:`products.Product` to add.

    **Effects:**
    - Creates a new :model:`user_profiles.Wishlist`
      entry if not already present.
    - Displays a success message on completion.

    **Redirects:**
    - Redirects back to the user's profile page.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(
        user=request.user, product=product
    )

    if created:
        messages.success(request, f"{product.title} added to your wishlist.")
    else:
        messages.info(request, f"{product.title} is already in your wishlist.")

    return redirect("view_bag")


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist.

    Deletes the wishlist entry for the given product belonging
    to the current user.

    **Args:**
    ``product_id``
        Primary key of the :model:`products.Product` to remove.

    **Effects:**
    - Deletes the :model:`user_profiles.Wishlist` entry for the product.
    - Displays an info message on completion.

    **Redirects:**
    - Redirects back to the user's profile page.
    """
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    messages.info(request, f"{product.title} removed from your wishlist.")
    return redirect("profile")


@login_required
def move_to_cart(request, product_id):
    """
    Move a product from the user's wishlist into the shopping cart.

    Adds the product to the session-based shopping bag and removes
    it from the wishlist to prevent duplication.

    **Args:**
    ``product_id``
        Primary key of the :model:`products.Product` to move.

    **Effects:**
    - Adds the product to the user's shopping bag (stored in session).
    - Deletes the corresponding :model:`user_profiles.Wishlist` entry.
    - Displays a success message on completion.

    **Redirects:**
    - Redirects back to :view:`bag:view_bag`, keeping the user on
      the shopping bag page.
    """
    product = get_object_or_404(Product, id=product_id)

    bag = request.session.get("bag", {})

    if str(product_id) in bag:
        bag[str(product_id)]["quantity"] += 1
    else:
        bag[str(product_id)] = {"product_id": product_id, "quantity": 1}

    request.session["bag"] = bag

    Wishlist.objects.filter(user=request.user, product=product).delete()

    messages.success(
        request,
        f"{product.title} moved to your shopping bag."
    )
    return redirect("view_bag")
