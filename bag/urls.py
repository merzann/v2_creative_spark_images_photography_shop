from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<int:product_id>/', views.add_to_bag, name='add_to_bag'),
    path('update/<item_key>/', views.update_bag_item, name='update_bag_item'),
    path("remove/<str:item_key>/",
         views.remove_from_bag,
         name='remove_from_bag',
         ),
]
