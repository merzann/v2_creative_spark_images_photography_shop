from django.urls import path
from .views import profile
from .views import request_account_deletion

urlpatterns = [
    path("", profile, name="profile"),
    path(
        "order-history/",
        lambda request: profile(request),
        name="order_history",
    ),
    path('delete-request/', request_account_deletion, name='delete_request'),
]
