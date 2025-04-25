from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path("load-guest-form/", views.load_guest_form, name="load_guest_form"),
    path('success/', views.checkout_success, name='checkout_success'),
    path(
        'create-checkout-session/',
        views.create_checkout_session,
        name='create_checkout_session',
    ),
]
