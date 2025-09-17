from django.contrib import admin
from django.urls import path, include
from .views import page_under_construction

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('newsletter/', include('newsletter.urls')),
    path("products/", include("products.urls")),
    path('profile/', include('user_profiles.urls')),
    path('shop/', include('shop.urls'), name='shop-urls'),
    path('summernote/', include('django_summernote.urls')),
    path(
        'under-construction/',
        page_under_construction,
        name='page_under_construction',
    ),
    path('', include('home.urls'), name='home-urls'),
]

# Custom 404 handler
handler404 = 'my_shop.views.handler404'
