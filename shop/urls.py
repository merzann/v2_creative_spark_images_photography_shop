from django.urls import path
from .views import gallery_page, images_by_theme
from products.views import product_detail

urlpatterns = [
    path("gallery/", gallery_page, name="gallery_page"),
    path("gallery/<slug:theme_slug>/", images_by_theme, name="images_by_theme"),
    path("<int:product_id>/", product_detail, name="product_detail"),
]
