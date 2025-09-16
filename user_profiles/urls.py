from django.urls import path

from . import views
from .views import profile
from .views import request_account_deletion

urlpatterns = [
    path("", profile, name="profile"),
    path(
        "order-history/",
        lambda request: profile(request),
        name="order_history",
    ),
    path(
        "wishlist/",
        lambda request: profile(request),
        name="wishlist",
    ),
    path('delete-request/', request_account_deletion, name='delete_request'),
    path(
        "wishlist/add/<int:product_id>/",
        views.add_to_wishlist,
        name="add_to_wishlist"
    ),
    path(
        "wishlist/remove/<int:product_id>/",
        views.remove_from_wishlist,
        name="remove_from_wishlist"
    ),
    path(
        "move-to-cart/<int:product_id>/",
        views.move_to_cart,
        name="move_to_cart"
    ),

]
