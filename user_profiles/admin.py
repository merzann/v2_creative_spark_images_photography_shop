from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
from django.http import HttpResponse
from .models import UserProfile
import csv


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for the `UserProfile` model.
    """

    list_display = (
        "first_name",
        "last_name",
        "language_preference",
        "email",
        "default_country"
    )
    search_fields = (
        "user__first_name",
        "user__last_name",
        "user__email",
        "default_country__name",
    )
    list_filter = ("language_preference", ("default_country", DropdownFilter),)
    actions = ['export_as_csv']

    def first_name(self, obj):
        return obj.user.first_name
    first_name.admin_order_field = "user__first_name"
    first_name.short_description = "First Name"

    def last_name(self, obj):
        return obj.user.last_name
    last_name.admin_order_field = "user__last_name"
    last_name.short_description = "Last Name"

    def email(self, obj):
        return obj.user.email
    email.admin_order_field = "user__email"
    email.short_description = "Email Address"

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        writer.writerow([
            "First Name",
            "Last Name",
            "Email",
            "Country",
            "Phone Number",
        ])

        for user in queryset:
            writer.writerow([
                user.user.first_name,
                user.user.last_name,
                user.user.email,
                user.default_country.name if user.default_country else "N/A",
                user.default_phone_number or "N/A"
            ])

        return response

    export_as_csv.short_description = "Export Selected User Profiles as CSV"
