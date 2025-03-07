from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import DigitalProduct, PrintedProduct, OrderModel


class DigitalProductModelTest(TestCase):
    """
    Test the DigitalProduct model for validation, creation, and deletion.
    """

    def setUp(self):
        """Create a sample DigitalProduct for testing."""
        self.digital_product = DigitalProduct.objects.create(
            title="Sunset in Ireland",
            description="A beautiful sunset photo",
            theme="Sunset",
            price=29.99,
            license_type="personal",
        )

    def test_digital_product_creation(self):
        """Test if the DigitalProduct instance is correctly created."""
        self.assertEqual(self.digital_product.title, "Sunset in Ireland")
        self.assertEqual(DigitalProduct.objects.count(), 1)

    def test_digital_product_deletion(self):
        """Test if the DigitalProduct instance is correctly deleted."""
        self.digital_product.delete()
        self.assertEqual(DigitalProduct.objects.count(), 0)


class PrintedProductModelTest(TestCase):
    """
    Test the PrintedProduct model for validation, creation, and deletion.
    """

    def setUp(self):
        """Create a sample PrintedProduct for testing."""
        self.printed_product = PrintedProduct.objects.create(
            title="Cliffs of Moher",
            description="Stunning view of Cliffs of Moher",
            theme="Landscape",
            print_type="canvas",
            size="20x30 cm",
            price=49.99,
        )

    def test_printed_product_creation(self):
        """Test if the PrintedProduct instance is correctly created."""
        self.assertEqual(self.printed_product.print_type, "canvas")
        self.assertEqual(PrintedProduct.objects.count(), 1)

    def test_printed_product_deletion(self):
        """Test if the PrintedProduct instance is correctly deleted."""
        self.printed_product.delete()
        self.assertEqual(PrintedProduct.objects.count(), 0)


class OrderModelTest(TestCase):
    """
    Test the OrderModel for validation, creation, and deletion.
    """

    def setUp(self):
        """Create a user and sample order for testing."""
        self.user = User.objects.create_user(
            username="testuser",
            password="securepassword",
        )
        self.digital_product = DigitalProduct.objects.create(
            title="Sunset in Ireland",
            description="A beautiful sunset photo",
            theme="Sunset",
            price=29.99,
            license_type="personal",
        )
        self.printed_product = PrintedProduct.objects.create(
            title="Cliffs of Moher",
            description="Stunning view of Cliffs of Moher",
            theme="Landscape",
            print_type="canvas",
            size="20x30 cm",
            price=49.99,
        )
        self.order = OrderModel.objects.create(
            user=self.user,
            total_price=79.98,
        )
        self.order.digital_products.add(self.digital_product)
        self.order.printed_products.add(self.printed_product)

    def test_order_creation(self):
        """Test if the OrderModel instance is correctly created."""
        self.assertEqual(self.order.user.username, "testuser")
        self.assertEqual(self.order.digital_products.count(), 1)
        self.assertEqual(self.order.printed_products.count(), 1)
        self.assertEqual(OrderModel.objects.count(), 1)

    def test_order_deletion(self):
        """Test if the OrderModel instance is correctly deleted."""
        self.order.delete()
        self.assertEqual(OrderModel.objects.count(), 0)
