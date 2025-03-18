from django.test import TestCase
from django.utils.timezone import now, timedelta
from django.urls import reverse
from home.models import SpecialOffer


class SpecialOfferViewTest(TestCase):
    """
    Test cases for the views rendering the homepage and shop.
    """

    def setUp(self):
        """
        Set up test offers.
        """
        self.offer = SpecialOffer.objects.create(
            text="Holiday Sale!",
            expiry_date=now() + timedelta(days=5)
        )

    def test_home_view_with_special_offer(self):
        """
        Ensure the homepage correctly renders with the latest special offer.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        self.assertIn("special_offer", response.context)
        self.assertEqual(response.context["special_offer"], self.offer)

    def test_home_view_without_special_offer(self):
        """
        Ensure the homepage renders correctly when no special offers exist.
        """
        SpecialOffer.objects.all().delete()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        self.assertIsNone(response.context["special_offer"])

    def test_shop_view(self):
        """
        Ensure the shop page renders successfully.
        """
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop.html")
