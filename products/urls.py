from django.urls import path
from .views import product_detail, image_licenses

urlpatterns = [
    path("<int:product_id>/", product_detail, name="product_detail"),
    path("licenses/", image_licenses, name="image_licenses"),
]
