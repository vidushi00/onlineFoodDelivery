from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign-up/', views.RegisterViewApi.as_view(), name='sign-up'),
    path('sign-in/', views.login_user, name='sign-in')
]
