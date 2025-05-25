from django.urls import path
from .views import (
    save_profile_from_checkout,
    load_billing_form,
    save_billing_from_checkout,
)
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path("load-guest-form/", views.load_guest_form, name="load_guest_form"),
    path(
        'save-profile-from-checkout/',
        save_profile_from_checkout,
        name='save_profile_from_checkout',
    ),
    path('load-billing-form/', load_billing_form, name='load_billing_form'),
    path(
        'save-billing-from-checkout/',
        save_billing_from_checkout,
        name='save_billing_from_checkout',
    ),
    path('summary/', views.checkout_summary, name='checkout_summary'),
    path('success/', views.checkout_success, name='checkout_success'),
    path(
        'create-checkout-session/',
        views.create_checkout_session,
        name='create_checkout_session',
    ),
]
