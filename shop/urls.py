from django.urls import path
from products.views import product_detail
from .views import gallery_page, images_by_theme, PolicyPageView

urlpatterns = [
    path("gallery/", gallery_page, name="gallery_page"),
    path(
        "gallery/<slug:theme_slug>/",
        images_by_theme,
        name="images_by_theme",
    ),
    path('policy/<slug:slug>/', PolicyPageView.as_view(), name='policy_page'),
    path("<int:product_id>/", product_detail, name="product_detail"),
]
