from django.urls import path
from .views import save_profile_from_checkout
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path("load-guest-form/", views.load_guest_form, name="load_guest_form"),
    path('success/', views.checkout_success, name='checkout_success'),
    path(
        'save-profile-from-checkout/',
        save_profile_from_checkout,
        name='save_profile_from_checkout',
    ),
]
