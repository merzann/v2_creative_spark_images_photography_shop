"""
URL configuration for my_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
handler404 = 'my_shop.views.handler404'
