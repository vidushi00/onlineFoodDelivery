from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkout-session/', views.create_checkout_session, name='checkout-session'),
    path('payment/success/', views.payment_success, name='payment-success'),
    path('payment/fail', views.payment_fail, name='payment-fail'),
    path('webhook-stripe/', views.webhook_view, name='webhook-stripe'),
    path('user/<int:user_id>', views.get_all_orders_by_user, name='get-user-order')
]