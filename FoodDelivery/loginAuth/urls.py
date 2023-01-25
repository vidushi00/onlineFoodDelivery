from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.RegisterViewApi.as_view(), name='sign-up'),
    path('signin/', views.login_user, name='sign-in')
]
