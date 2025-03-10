from django.test import TestCase
from django.contrib.auth.models import User
from user_profiles.models import UserProfile


class UserProfileSignalTest(TestCase):
    """
    Tests that the UserProfile is automatically created and updated by signals.
    """

    def test_profile_creation_signal(self):
        """Test that a UserProfile is created when a User is registered."""
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.assertTrue(UserProfile.objects.filter(user=user).exists())

    def test_profile_auto_save_signal(self):
        """Test that UserProfile updates when User is saved."""
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        user.email = "newemail@example.com"
        user.save()
        self.assertEqual(user.userprofile.user.email, "newemail@example.com")
