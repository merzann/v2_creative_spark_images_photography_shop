from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from django.http import HttpResponse
from .models import UserProfile
import csv


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `UserProfile Model` model.
    """

    list_display = ("user", "language_preference", "email", "default_country")
    search_fields = ("user__username", "user__email", "country__name",)
    list_filter = ("language_preference", ("default_country", DropdownFilter),)
    actions = ['export_as_csv']

    def email(self, obj):
        """Fetch email from related User model."""
        return obj.user.email
    email.admin_order_field = "user__email"
    email.short_description = "Email Address"

    def export_as_csv(self, request, queryset):
        """
        Exports selected users as a CSV file.

        Generates a CSV file with user details and provides it as a
        downloadable response.

        **CSV Fields:**
        - ``Username``
        - ``Email``
        - ``Country``
        - ``Phone Number``
        """

        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow(["Username", "Email", "Country", "Phone Number"])

        for user in queryset:
            writer.writerow([
                user.user.username,
                user.user.email,
                user.default_country.name if user.default_country else "N/A",
                user.default_phone_number or "N/A"
            ])

        return response

    export_as_csv.short_description = "Export Selected User Profiles as CSV"
