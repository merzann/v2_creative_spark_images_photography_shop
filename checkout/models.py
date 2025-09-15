from django.db import models
from django.contrib.auth.models import User


class CheckoutSession(models.Model):
    bag_id = models.CharField(max_length=64, unique=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    bag_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CheckoutSession {self.bag_id} for {self.user}"
