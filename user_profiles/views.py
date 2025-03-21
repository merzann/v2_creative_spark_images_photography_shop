from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Handles the user profile page for :model:`user_profiles.UserProfile`,
    allowing users to view and update their profile details.

    **Context:**

    `form`
        An instance of :form:`user_profiles.UserProfileForm` for updating
        user information.

    **Template:**

    :template:`user_profiles/profile.html`
    """

    user_profile = request.user.userprofile

    if request.method == "POST":
        form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=user_profile,
        )
        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "user_profiles/profile.html", {"form": form})


@login_required
def request_account_deletion(request):
    """
    Handle a user-submitted request to delete their account.

    A POST request triggers an email to the site administrator containing
    the user's information and their
    optional message.

    **Context:**

    This view does not render a template. It redirects to the
    "profile" page after handling the request.

    **Request Method:**

    - ``POST``: Sends the deletion request via email.

    **Behavior:**

    - On success, a success message is shown and the user is redirected.
    - On non-POST requests, the view immediately redirects.

    **Email Content:**

    - Username and email of the requesting user.
    - Optional message provided in the request.

    **Redirects:**

    :redirect:`profile`
    """
    if request.method == "POST":
        message = request.POST.get("message", "No message provided.")
        user = request.user
        email_body = (
            f"User {user.username} ({user.email}) has requested "
            f"account deletion.\n\nMessage:\n{message}"
        )

        # You can save this to the DB instead of emailing if preferred
        send_mail(
            subject="Account Deletion Request",
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
        )

        messages.success(request, "Your request has been submitted.")
    return redirect("profile")
