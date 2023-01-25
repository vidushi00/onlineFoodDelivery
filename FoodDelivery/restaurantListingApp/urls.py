from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_all_restaurants, name='all_restaurants'),
    path('get/<int:id>', views.get_restaurant_by_id, name='get-restaurant'),
    path('save/', views.post_restaurant_details, name='save-restaurant'),
]