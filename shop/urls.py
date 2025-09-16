from django.urls import path
from products.views import image_licenses, product_detail
from .views import ContactPage, gallery_page, images_by_theme, PolicyPageView
from .dashboard import sales_dashboard

urlpatterns = [
    path('contact/', ContactPage.as_view(), name='contact_page'),
    path("gallery/", gallery_page, name="gallery_page"),
    path(
        "gallery/<slug:theme_slug>/",
        images_by_theme,
        name="images_by_theme",
    ),
    path('policy/<slug:slug>/', PolicyPageView.as_view(), name='policy_page'),
    path("<int:product_id>/", product_detail, name="product_detail"),
    path('licenses/', image_licenses, name='license_info'),
    path("dashboard/", sales_dashboard, name="sales_dashboard"),
]
