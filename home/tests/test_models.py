from django.test import TestCase
from django.utils.timezone import now, timedelta
from home.models import SpecialOffer


class SpecialOfferModelTest(TestCase):
    """
    Test cases for the SpecialOffer model.
    """

    def setUp(self):
        """
        Create sample special offers for testing.
        """
        self.offer1 = SpecialOffer.objects.create(
            text="Limited Time Offer!",
            expiry_date=now() + timedelta(days=1)
        )
        self.offer2 = SpecialOffer.objects.create(
            text="Weekend Discount!",
            expiry_date=now() + timedelta(days=2)
        )

    def test_string_representation(self):
        """
        Ensure the
        string representation of SpecialOffer is correctly formatted.
        """
        self.assertEqual(
            str(self.offer1),
            f"Special Offer (Expires: {self.offer1.expiry_date})"
        )

    def test_ordering_by_expiry_date(self):
        """
        Ensure the latest offer is retrieved correctly.
        """
        latest_offer = SpecialOffer.objects.order_by('-expiry_date').first()
        self.assertEqual(latest_offer, self.offer2)
