from django.db import models


class NewsletterSignup(models.Model):
    """
    Stores email addresses of users who subscribe to the newsletter.

    **Usage:**

    Used to collect and manage newsletter subscribers across the site.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"
