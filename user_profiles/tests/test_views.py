from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class ProfileViewTest(TestCase):
    """
    Test cases for the user profile view, ensuring correct access control
    and template rendering.
    """

    def setUp(self):
        """Set up a test user and log them in."""
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.client.login(username="testuser", password="testpassword")

    def test_profile_page_loads(self):
        """Test that the profile page loads correctly for a logged-in user."""
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user_profiles/profile.html")

    def test_profile_requires_login(self):
        """Test that unauthenticated users are redirected to login."""
        self.client.logout()
        response = self.client.get(reverse("profile"))
        self.assertEqual(response.status_code, 302)  # Redirect to login
