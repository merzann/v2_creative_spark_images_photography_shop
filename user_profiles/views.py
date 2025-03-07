from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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
            return redirect("profile")  # Redirect to profile page

    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, "user_profiles/profile.html", {"form": form})
