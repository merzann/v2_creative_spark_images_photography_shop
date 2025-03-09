from django.test import TestCase
from django.contrib.auth.models import User
from user_profiles.models import UserProfile
from django_countries.fields import Country


class UserProfileModelTest(TestCase):
    """
    Unit tests for the UserProfile model.
    """

    def setUp(self):
        """
        Set up a test user and associated UserProfile.
        """
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="testpassword",
        )
        self.profile = UserProfile.objects.get(user=self.user)

    def test_profile_creation(self):
        """
        Ensure a UserProfile is created when a new User is registered.
        """
        self.assertEqual(self.profile.user.username, "testuser")
        self.assertEqual(UserProfile.objects.count(), 1)

    def test_profile_fields(self):
        """
        Check default values of UserProfile fields.
        """
        self.assertEqual(self.profile.language_preference, "en")
        self.assertIsNone(self.profile.default_phone_number)

    def test_country_field(self):
        """
        Validate the default country value.
        """
        self.profile.default_country = Country("DE")
        self.profile.save()
        self.assertEqual(self.profile.default_country.code, "DE")
