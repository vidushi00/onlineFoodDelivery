from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all-restaurants', views.get_all_restaurants, name='all_restaurants'),
    path('get-restaurant/<int:id>', views.get_restaurant_by_id, name='get-restaurant'),
    path('save-restaurant', views.post_restaurant_details, name='save-restaurant'),
]