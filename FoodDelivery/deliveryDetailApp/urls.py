from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:user_id>', views.get_delivery_detail_by_user_id, name='get-user-delivery'),
    path('add/detail', views.save_delivery_detail, name='add-delivery-detail')
    ]