from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-users-cart/<int:user_id>', views.get_all_items_by_user_id, name='get-users-cart'),
    path('add-item', views.add_item_to_cart, name='add-item'),
    path('remove-item/<int:id>', views.remove_item_from_cart, name='remove-item'),
]