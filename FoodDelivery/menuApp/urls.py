from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-restaurant-menu/<int:restaurant_id>', views.get_all_menu_by_restaurant_id, name='get-restaurant-menu'),
    path('get-menu/<int:id>', views.get_menu_by_id, name='get-menu'),
    path('save-menu-details', views.post_menu_details, name='save-menu-details'),
]