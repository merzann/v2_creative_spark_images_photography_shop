# newsletter/admin.py
from django.contrib import admin
from .models import NewsletterSignup
import csv
from django.http import HttpResponse


@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    """
    Admin interface for managing newsletter signups.

    Displays subscriber email, first name, last name, and signup timestamp.
    Includes an admin action to export selected signups as a CSV file.
    """
    list_display = ('email', 'first_name', 'last_name', 'timestamp')
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = (
            'attachment; filename="newsletter_signups.csv"'
        )
        writer = csv.writer(response)
        writer.writerow(['Email', 'First Name', 'Last Name', 'Timestamp'])
        for signup in queryset:
            writer.writerow([
                signup.email,
                signup.first_name,
                signup.last_name,
                signup.timestamp
            ])
        return response

    export_as_csv.short_description = "Export selected to CSV"
