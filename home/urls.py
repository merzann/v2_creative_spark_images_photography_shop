from django.urls import path
from .views import about_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about_view, name='about'),
    path('shop/', views.shop, name='shop'),
]
