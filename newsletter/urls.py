from django.urls import path
from . import views
from .views import newsletter_signup

urlpatterns = [
    path('', views.newsletter_signup_page, name='newsletter_page'),
    path('newsletter-signup/', newsletter_signup, name='newsletter_signup'),
]
