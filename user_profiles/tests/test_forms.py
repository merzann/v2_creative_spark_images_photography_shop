from django.test import TestCase
from user_profiles.forms import UserProfileForm


class UserProfileFormTest(TestCase):
    """
    Tests for the UserProfileForm.
    """

    def test_form_valid_data(self):
        """Test form validation with correct data."""
        form = UserProfileForm(data={
            "language_preference": "fr",
            "default_phone_number": "123456789",
            "default_country": "FR",
            "default_postcode": "75001",
            "default_town_or_city": "Paris",
            "default_street_address1": "123 Champs Elysees",
        })
        self.assertTrue(form.is_valid())

    def test_form_missing_required_fields(self):
        """Test form fails validation when required fields are missing."""
        form = UserProfileForm(data={})
        self.assertFalse(form.is_valid())
