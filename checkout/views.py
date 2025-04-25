from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.forms import BillingForm


def billing_information(request):
    """
    Collect and validate billing details using :form:`checkout.BillingForm`.

    Prepopulates the form with data from :model:`user_profiles.UserProfile`
    if the user is authenticated. On POST, the data is saved to the session
    and the user is redirected to the next step in checkout.

    **Context:**

    ``form``
        A form instance for collecting billing details.

    **Template:**
    :template:`checkout/billing.html`

    **Redirects:**
    :redirect:`product_preview`
    """
    if request.user.is_authenticated:
        profile = request.user.userprofile
        form = BillingForm(instance=profile)
    else:
        form = BillingForm()

    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            # Store data in session
            request.session["billing_data"] = form.cleaned_data
            return redirect("product_preview")  # Next step in checkout
        else:
            messages.warning(request, "Please complete all required fields.")

    return render(request, "checkout/billing.html", {"form": form})
