from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth.models import User


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
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data["email"]
            user.save()
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserProfileForm(instance=user_profile, user=request.user)

    return render(request, "user_profiles/profile.html", {"form": form})
