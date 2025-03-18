from django.db import models


class SpecialOffer(models.Model):
    """
    Represents a special offer with a promotional message and an
    expiry date.

    Attributes:
        text (TextField): The promotional message of the special offer.
        expiry_date (DateTimeField): The date and time when the
            offer expires.
    """
    text = models.TextField(max_length=255)
    expiry_date = models.DateTimeField()

    def __str__(self):
        """
        Returns a string representation of the SpecialOffer instance.
        """
        return f"Special Offer (Expires: {self.expiry_date})"
