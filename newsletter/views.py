from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from .models import NewsletterSignup
from .forms import NewsletterForm


@require_POST
def newsletter_signup(request):
    """
    Handle newsletter signup form submission.

    Validates and saves the submitted email address using
    :form:`newsletter.NewsletterForm`. Displays a success or error
    message and redirects the user.

    **Redirects:**
        - On success or failure, redirects to the referring page.

    **Messages:**
        - success or error messages shown via Django's messages framework.
    """
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        email = request.POST.get('email')

        if NewsletterSignup.objects.filter(email=email).exists():
            messages.warning(
                request,
                "⚠ You have already signed up to the newsletter."
            )
        elif form.is_valid():
            form.save()
            messages.success(request, "Thank you for signing up!")
        else:
            messages.error(
                request,
                "⚠ There was a problem with your submission. Please try again."
            )

    return redirect(request.META.get("HTTP_REFERER", "/"))
