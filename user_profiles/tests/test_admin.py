from django.test import TestCase
from django.contrib.auth.models import User
from user_profiles.admin import UserProfileAdmin
from user_profiles.models import UserProfile
from django.contrib.admin.sites import site
from io import StringIO
import csv


class UserProfileAdminTest(TestCase):
    """
    Tests for the UserProfileAdmin class, including CSV export.

    Related Models:
    - user_profiles.models.UserProfile

    Related Files:
    - user_profiles.admin.UserProfileAdmin
    """

    def setUp(self):
        """
        Set up an admin user and test users.
        """
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
        )
        self.user1 = User.objects.create_user(
            username="testuser1",
            email="test1@example.com",
            password="testpassword1",
        )
        self.user2 = User.objects.create_user(
            username="testuser2",
            email="test2@example.com",
            password="testpassword2",
        )

        self.client.login(username="admin", password="adminpassword")

    def test_export_csv(self):
        """
        Ensure that exporting users as CSV works correctly.
        """
        user_profile_admin = UserProfileAdmin(UserProfile, site)
        queryset = UserProfile.objects.filter(
            user__username__startswith="testuser"
        )

        response = user_profile_admin.export_as_csv(None, queryset)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response["Content-Type"], "text/csv")

        content = response.content.decode("utf-8")
        csv_reader = csv.reader(StringIO(content))
        rows = list(csv_reader)

        # Check CSV headers
        self.assertEqual(rows[0], [
            "Username", "Email", "Country", "Phone Number"
        ])

        # Ensure user rows exist
        self.assertEqual(len(rows) - 1, 2)
