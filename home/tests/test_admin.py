from django.test import TestCase
from django.utils.timezone import now, timedelta
from django.contrib.admin.sites import site
from home.models import SpecialOffer
from home.admin import SpecialOfferAdmin


class SpecialOfferAdminTest(TestCase):
    """
    Test cases for the SpecialOffer model in Django admin.
    """

    def setUp(self):
        """
        Create an instance of the admin model.
        """
        self.offer = SpecialOffer.objects.create(
            text="Admin Panel Test Offer",
            expiry_date=now() + timedelta(days=3)
        )
        self.admin = SpecialOfferAdmin(SpecialOffer, site)

    def test_admin_displayed_fields(self):
        """
        Ensure the correct fields are displayed in Django admin.
        """
        self.assertEqual(
            self.admin.get_list_display(None),
            ('text', 'expiry_date')
        )

    def test_admin_ordering(self):
        """
        Ensure offers are ordered by expiry_date in descending order.
        """
        self.assertEqual(self.admin.ordering, ('-expiry_date',))

    def test_admin_summernote_integration(self):
        """
        Ensure Summernote is enabled for the `text` field.
        """
        self.assertIn('text', self.admin.summernote_fields)
